# Module tester

from algorithms.bt import bt
from algorithms.mac_bt import mac_bt
from algorithms.bj import bj
from algorithms.dbt import dbt
from constants import (
  N,
  CAT_KEY,
  INST_KEY,
  SOL_KEY,
  BT,
  MAC_BT,
  BJ,
  DBT,
  STMT,
  SETUP,
)
from examples import examples
from helpers import (
  duplicate_sudoku,
  output,
)
from timeit import timeit

def run(algorithm, verbose):
  print("")
  for num, example in enumerate(examples):
    sudoku = duplicate_sudoku(example[INST_KEY])

    if algorithm == BT:
      bt(sudoku)
    elif algorithm == MAC_BT:
      mac_bt(sudoku)
    elif algorithm == BJ:
      bj(sudoku)
    elif algorithm == DBT:
      dbt(sudoku)

    cpu_time = timeit(stmt = STMT, setup = SETUP, number = 1, globals = locals()) * 1000

    error = 0
    for i in range(N):
      for j in range(N):
        if sudoku[i][j] != example[SOL_KEY][i][j]:
          error = 1
    
    if verbose:
      print("=========================")
      print("[SUDOKU " + str(num + 1) + "]")
      print("=========================")
      print("Category: " + example[CAT_KEY])
      print("Result: " +  ("ERROR" if error else "SUCCESS"))
      print("CPU time: " + str(format(cpu_time, ".3f")) + " MS")
      print("Input:")
      output(example[INST_KEY])
      print("Output:")
      output(sudoku)
      print("Expected:")
      output(example[SOL_KEY])
    else:
      print("[SUDOKU " + str(num + 1) + "]", end = " ")
      print("category: " + example[CAT_KEY], end = ", ")
      print("result: " +  ("ERROR" if error else "SUCCESS"), end = ", ")
      print("cpu_time: " + str(format(cpu_time, ".3f")) + " MS")
  print("")
