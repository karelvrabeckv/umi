# Module mac_bt

from constants import (
  N,
  VALUES,
)
from helpers import (
  duplicate_domains,
  get_empty_cell,
  check_constraints,
)

"""
Solve a sudoku with CHRONOLOGICAL
BACKTRACKING using ADVANCED
FILTERING (meaning maintaining
arc consistency).
"""
def mac_bt(sudoku):
  # Create a duplicate of the sudoku
  # that contains all domain values
  # from 1 to 9 in the case of unset
  # variables. If a variable is set, 
  # there is only one specific value
  global domains
  domains = [
    [
      [*VALUES] if not sudoku[row][col] else [sudoku[row][col]]
      for col in range(N)
    ]
    for row in range(N)
  ]
  return run(sudoku)

def run(sudoku):
  global domains

  # Look for the next empty cell.
  # If there is no empty cell, finish
  # (the sudoku is filled)
  coords = []
  if not get_empty_cell(sudoku, coords):
    return True
  row, col = coords
  
  # Try assigning values from the domain
  for val in [*domains[row][col]]:
    # Check if the constraint (unequality
    # between row, column and box cells)
    # is followed
    if check_constraints(sudoku, row, col, val):
      # Set the current value and
      # save the current domains
      sudoku[row][col] = val
      original_domains = duplicate_domains(domains)

      # Filter the domain values
      # of the other cells
      if apply_advanced_filter(row, col, val):
        # Continue to the next
        # empty cell
        if run(sudoku):
          return True

      # Undo all the changes if
      # the next empty cells were
      # filled wrong
      domains = original_domains
      sudoku[row][col] = 0

  return False

def apply_advanced_filter(row, col, val):
  domains[row][col] = [val]

  # Fill a queue with all the arcs 
  # that are constrained (the values
  # of all those variables must be
  # unequal)
  queue = get_arcs()
  
  # Process all the constrained arcs
  while queue:
    x_i, x_j = queue.pop(0)

    # Modify the domain of x_i
    # according to the constraint
    # between x_i and x_j (unequality)
    if revise(x_i, x_j):
      # The domain of x_i has changed.
      # Some values were deleted. If there
      # is no value in the domain, finish
      if not domains[x_i[0]][x_i[1]]:
        return False
      
      # Add all the neighbours (except
      # x_j) into the queue
      add_neighbours(x_i, x_j, queue)

  return True

def get_arcs():
  arcs = []
  for row in range(N):
    for col in range(N):
      # Get the arcs from the current row
      for j in range(N):
        if j != col:
          arcs.append(((row, col), (row, j)))

      # Get the arcs from the current column
      for i in range(N):
        if i != row:
          arcs.append(((row, col), (i, col)))
      
      # Get the arcs from the current box
      box_i = row - row % 3
      box_j = col - col % 3
      for i in range(N // 3):
        for j in range(N // 3):
          if (box_i + i != row) and (box_j + j != col):
            arcs.append(((row, col), (box_i + i, box_j + j)))
  return arcs

def revise(x_i, x_j):
  revised = False

  # Loop through the domain of x_i
  for x in [*domains[x_i[0]][x_i[1]]]:
    value_to_delete = True

    # Loop through the domain of x_j
    for y in domains[x_j[0]][x_j[1]]:
      # Check the constraint
      if x != y:
        value_to_delete = False

    # Delete the value from
    # the domain of x_i if it
    # has no support
    if value_to_delete:
      domains[x_i[0]][x_i[1]].remove(x)
      revised = True

  return revised

def add_neighbours(x_i, x_j, queue):
  x_i_row, x_i_col = x_i[0], x_i[1]
  x_j_row, x_j_col = x_j[0], x_j[1]

  # Get the neighbours from the current row
  for j in range(N):
    # Avoid x_i and x_j
    if (j != x_i_col) and ((x_i_row != x_j_row) or (j != x_j_col)):
      queue.append(((x_i_row, j), (x_i_row, x_i_col)))

  # Get the neighbours from the current column
  for i in range(N):
    # Avoid x_i and x_j
    if (i != x_i_row) and ((i != x_j_row) or (x_i_col != x_j_col)):
      queue.append(((i, x_i_col), (x_i_row, x_i_col)))

  # Get the neighbours from the current box
  box_i = x_i_row - x_i_row % 3
  box_j = x_i_col - x_i_col % 3
  for i in range(N // 3):
    for j in range(N // 3):
      # Avoid x_i and x_j
      if (box_i + i != x_i_row) and (box_j + j != x_i_col):
        if (box_i + i != x_j_row) or (box_j + j != x_j_col):
          queue.append(((box_i + i, box_j + j), (x_i_row, x_i_col)))
