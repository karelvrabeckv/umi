# Module bj

from constants import N
from helpers import (
  get_empty_cell,
  get_vals,
)

"""
Solve a sudoku with BACKJUMPING.
"""
def bj(sudoku):
  # Create a duplicate of the sudoku
  # that contains all FEASIBLE domain
  # values in the case of unset
  # variables. If a variable is set,
  # there is only one specific value
  global domains
  domains = [
    [
      get_vals(sudoku, row, col) if not sudoku[row][col] else [sudoku[row][col]]
      for col in range(N)
    ]
    for row in range(N)
  ]
  return run(sudoku)

def run(sudoku):
  # Look for the next empty cell.
  # If there is no empty cell, finish
  # (the sudoku is filled)
  coords = []
  if not get_empty_cell(sudoku, coords):
    return (True, {})
  row, col = coords
  answer, conflict_set = False, set()

  # Try assigning values from the domain
  for val in domains[row][col]:
    # Check if the constraint (unequality
    # between row, column and box cells)
    # is followed. If not, get all the
    # conflicting variables
    followed, new_conflicts = check_conflicts(sudoku, row, col, val)

    if followed:
      # Set the value and continue
      # with the next empty cell
      sudoku[row][col] = val
      answer, new_conflicts = run(sudoku)

    if answer:
      # The next empty cells were
      # filled correctly, so it can
      # be successfully finished
      return (answer, {})
    elif (row, col) not in new_conflicts:
      # One of the next empty cells
      # was not filled, because it had
      # so much conflicts in the
      # previous cells. So it is jumping
      # back to the last of these
      # conflicts. Also, the sudoku must
      # be reset until it
      sudoku[row][col] = 0
      return (False, new_conflicts)
    else:
      # All feasible values are being
      # tested. It is gathering all of
      # their conflicts
      conflict_set.update(new_conflicts)
      conflict_set.remove((row, col))

  # None of the values is feasible,
  # so it is reset and returned back
  # to the nearest conflict
  sudoku[row][col] = 0
  return (False, conflict_set)

def check_conflicts(sudoku, row, col, val):
  conflicts = set()

  # Check the values in the row
  for j in range(N):
    if sudoku[row][j] == val:
      conflicts.add((row, j))

  # Check the values in the column
  for i in range(N):
    if sudoku[i][col] == val:
      conflicts.add((i, col))

  # Check the values in the box
  box_i = row - row % 3
  box_j = col - col % 3
  for i in range(N // 3):
    for j in range(N // 3):
      if (box_i + i != row) and (box_j + j != col) and (sudoku[box_i + i][box_j + j] == val):
        conflicts.add((box_i + i, box_j + j))

  return (True, {}) if not conflicts else (False, {*conflicts, (row, col)})
