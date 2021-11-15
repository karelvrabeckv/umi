# Module constants

N = 9
VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ALLOWED = "ALLOWED"

BT = "BT"
MAC_BT = "MAC_BT"
BJ = "BJ"
DBT = "DBT"

CAT_KEY = "category"
INST_KEY = "instance"
SOL_KEY = "solution"

CAT_EASY = "EASY"
CAT_MEDIUM = "MEDIUM"
CAT_HARD = "HARD"
CAT_VERY_HARD = "VERY HARD"

STMT = """
sudoku = duplicate_sudoku(example[INST_KEY])

if algorithm == BT:
  bt(sudoku)
elif algorithm == MAC_BT:
  mac_bt(sudoku)
elif algorithm == BJ:
  bj(sudoku)
elif algorithm == DBT:
  dbt(sudoku)
"""

SETUP = """
from algorithms.bt import bt
from algorithms.mac_bt import mac_bt
from algorithms.bj import bj
from algorithms.dbt import dbt
from constants import (
  INST_KEY,
  BT,
  MAC_BT,
  BJ,
  DBT,
)
from helpers import duplicate_sudoku
"""
