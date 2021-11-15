from constants import (
  BT,
  MAC_BT,
  BJ,
  DBT,
)
from sys import argv
from tester import run

# Check the number of arguments
if len(argv) not in {2, 3}:
  print("[ERROR] Wrong number of arguments.")
  exit()

# Check the algorithm
if argv[1] not in {BT, MAC_BT, BJ, DBT}:
  print("[ERROR] Wrong algorithm.")
  exit()

# Check the option
if len(argv) == 3 and argv[2] != "-v":
  print("[ERROR] Wrong option.")
  exit()

# Solve all the examples of sudoku
run(argv[1], False if (len(argv) == 2) else True)
