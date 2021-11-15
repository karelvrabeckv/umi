# Module bt

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
BACKTRACKING using BASIC FILTERING
(meaning forward checking).
"""
def bt(sudoku):
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
      # of the other cells in
      # the row, column and box
      if apply_basic_filter(row, col, val):
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

def apply_basic_filter(row, col, val):
  # Modify the domain values in the row
  for j in range(N):
    if (j != col) and (val in domains[row][j]):
      domains[row][j].remove(val)
      if not domains[row][j]:
        return False

  # Modify the domain values in the column
  for i in range(N):
    if (i != row) and (val in domains[i][col]):
      domains[i][col].remove(val)
      if not domains[i][col]:
        return False

  # Modify the domain values in the box
  box_i = row - row % 3
  box_j = col - col % 3
  for i in range(N // 3):
    for j in range(N // 3):
      if (box_i + i != row) and (box_j + j != col) and (val in domains[box_i + i][box_j + j]):
        domains[box_i + i][box_j + j].remove(val)
        if not domains[box_i + i][box_j + j]:
          return False

  return True
