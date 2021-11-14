# Module tester

from algorithms.bt import bt
from algorithms.mac_bt import mac_bt
from algorithms.bj import bj
from algorithms.dbt import dbt
from algorithms.ddbt import ddbt
from constants import (
  N,
  CAT_KEY,
  INST_KEY,
  SOL_KEY,
  BT,
  MAC_BT,
  BJ,
  DBT,
  DDBT,
)
from examples import examples
from helpers import (
  duplicate_sudoku,
  output,
)
from time import process_time

def run(algorithm, verbose):
  for num, example in enumerate(examples):
    sudoku = duplicate_sudoku(example[INST_KEY])

    start = process_time() * 1000
    if algorithm == BT:
      bt(sudoku)
    elif algorithm == MAC_BT:
      mac_bt(sudoku)
    elif algorithm == BJ:
      bj(sudoku)
    elif algorithm == DBT:
      dbt(sudoku)
    elif algorithm == DDBT:
      ddbt(sudoku)
    end = process_time() * 1000

    error = 0
    for i in range(N):
      for j in range(N):
        if sudoku[i][j] != example[SOL_KEY][i][j]:
          error = 1
    
    if verbose:
      print("")
      print("=========================")
      print("[SUDOKU " + str(num + 1) + "]")
      print("=========================")
      print("Category: " + example[CAT_KEY])
      print("Result: " +  ("ERROR" if error else "SUCCESS"))
      print("CPU time: " + str(format(end - start, ".3f")) + " MS")
      print("Input:")
      output(example[INST_KEY])
      print("Output:")
      output(sudoku)
      print("Expected:")
      output(example[SOL_KEY])
    else:
      if num == 0:
        print("")
      print("[SUDOKU " + str(num + 1) + "]", end = " ")
      print("category: " + example[CAT_KEY], end = ", ")
      print("result: " +  ("ERROR" if error else "SUCCESS"), end = ", ")
      print("CPU time: " + str(format(end - start, ".3f")) + " MS")

    if num + 1 == len(examples):
      print("")
