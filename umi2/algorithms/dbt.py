# Module dbt

from constants import (
  N,
  ALLOWED,
)
from helpers import (
  get_domain_values,
  get_empty_cell,
)

"""
Solve a sudoku with DYNAMIC
BACKTRACKING.
"""
def dbt(sudoku):
  # Create a duplicate of the sudoku
  # that contains all feasible domain
  # values in the case of unset
  # variables. If a variable is set,
  # there is only one specific value
  domains = [
    [
      get_domain_values(sudoku, row, col) if not sudoku[row][col] else [sudoku[row][col]]
      for col in range(N)
    ]
    for row in range(N)
  ]

  # Create a duplicate of the sudoku
  # to store conflicting variables
  # for each of the values from 1 to 9
  culprits = [[[ALLOWED for _ in range(N)] for _ in range(N)] for _ in range(N)]

  # Look for the next empty cell.
  # If there is no empty cell, finish
  # (the sudoku is filled)
  coords = []
  while get_empty_cell(sudoku, coords):
    row, col = coords

    # Process all the domain values
    # of the empty cell
    allowed = []
    for val in domains[row][col]:
      if culprits[row][col][val - 1] == ALLOWED:
        followed, conflicts = check_conflicts(sudoku, row, col, val)

        # Save the conflicts of all
        # the domain values of
        # the empty cell
        if not followed:
          culprits[row][col][val - 1] = conflicts
        else:
          allowed.append(val)

    if allowed:
      # There is at least one value
      # that follows all the constraints,
      # so it is set into the empty cell
      sudoku[row][col] = allowed.pop(0)
    else:
      # Create a conflict set as
      # the join of all the conflicts
      # of all the domain values
      conflict_set = set()
      for val in domains[row][col]:
        if culprits[row][col][val - 1] != ALLOWED:
          conflict_set.update(culprits[row][col][val - 1])

      if not conflict_set:
        # The sudoku has no solution
        # to return (for example if
        # the domain of the empty cell
        # is empty)
        return False
      else:
        # Jump back to the nearest
        # conflict
        n_c_row, n_c_col = max(conflict_set, key = lambda item: (item[0], item[1]))
        n_c_val = sudoku[n_c_row][n_c_col]

        # Reset all those culprits
        # where the nearest conflict
        # is contained
        for i in range(N):
          for j in range(N):
            for val in domains[i][j]:
              if (culprits[i][j][val - 1] != ALLOWED) and ((n_c_row, n_c_col) in culprits[i][j][val - 1]):
                culprits[i][j][val - 1] = ALLOWED

        # Save the whole conflict
        # set for the case that
        # the nearest conflict
        # will not have any domain
        # values to be set too
        culprits[n_c_row][n_c_col][n_c_val - 1] = conflict_set
        culprits[n_c_row][n_c_col][n_c_val - 1].remove((n_c_row, n_c_col))

        # Reset the value of
        # the nearest conflict
        sudoku[n_c_row][n_c_col] = 0

    # Delete the coordinates of
    # the empty cell, so it can
    # be used for the next
    coords.clear()

  return True

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

  return (True, {}) if not conflicts else (False, conflicts)
