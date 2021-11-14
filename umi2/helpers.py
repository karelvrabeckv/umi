# Module helpers

from constants import (
  N,
  VALUES,
)

"""
Duplicate domains.
"""
def duplicate_domains(domains):
  duplicate = [[[*domains[row][col]] for col in range(N)] for row in range(N)]
  return duplicate

"""
Duplicate a sudoku.
"""
def duplicate_sudoku(sudoku):
  duplicate = [[sudoku[row][col] for col in range(N)] for row in range(N)]
  return duplicate

"""
Get the coordinates of the next
empty cell.
"""
def get_empty_cell(sudoku, coords):
  for i in range(N):
    for j in range(N):
      if not sudoku[i][j]:
        coords.append(i)
        coords.append(j)
        return True
  return False

"""
Get all the feasible values
into the domain.
"""
def get_vals(sudoku, row, col):
  values = [*VALUES]

  # Discard values from the row
  for j in range(N):
    if sudoku[row][j] in values:
      values.remove(sudoku[row][j])

  # Discard values from the column
  for i in range(N):
    if sudoku[i][col] in values:
      values.remove(sudoku[i][col])

  # Discard values from the box
  box_i = row - row % 3
  box_j = col - col % 3
  for i in range(N // 3):
    for j in range(N // 3):
      if sudoku[box_i + i][box_j + j] in values:
        values.remove(sudoku[box_i + i][box_j + j])

  return values

"""
Check if the values in the row,
column and box are different
from the given value.
"""
def check_constraints(sudoku, row, col, val):
  # Check the values in the row/column
  for x in range(N):
    if (sudoku[row][x] == val) or (sudoku[x][col] == val):
      return False

  # Check the values in the box
  box_i = row - row % 3
  box_j = col - col % 3
  for i in range(N // 3):
    for j in range(N // 3):
      if sudoku[box_i + i][box_j + j] == val:
        return False

  return True

"""
Print a sudoku in a readable form.
"""
def output(sudoku):
  for i in range(N):
    if i % 3 == 0:
      print("+-------+-------+-------+")
    for j in range(N):
      if j % 3 == 0:
        print("|", end = " ")
      print(str(sudoku[i][j]), end = " ")
    print("|")
  print("+-------+-------+-------+")
