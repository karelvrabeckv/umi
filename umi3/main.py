from constants import (
  BT,
  DPLL,
)
from sys import argv
from tester import run

# Check the number of arguments
if len(argv) != 3:
  print("[ERROR] Wrong number of arguments.")
  exit()

# Check the algorithm
if argv[1] not in {BT, DPLL}:
  print("[ERROR] Wrong algorithm.")
  exit()

# Check the number of instances
try:
  if int(argv[2]) < 1 or int(argv[2]) > 50:
    raise ValueError
except ValueError:
  print("[ERROR] Wrong number of instances.")
  exit()

# Solve all the SATs
run(argv[1], int(argv[2]))
