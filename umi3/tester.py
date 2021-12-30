# Module tester

import numpy as np

from algorithms.bt import bt
from algorithms.dpll import dpll
from constants import (
  BASE,
  FOLDERS,
  BT,
  DPLL,
)
from loader import get_instance
from os import listdir
from time import process_time

"""
Run all the tests.
"""
def run(algorithm, limit):
  for folder in FOLDERS:
    files = listdir(BASE + folder["name"])

    results = []
    start = process_time() * 1000
    for file in files[0:limit]:
      clauses, literals = get_instance(BASE + folder["name"] + "/" + file)

      if algorithm == BT:
        result = bt(clauses, literals)
      elif algorithm == DPLL:
        result = dpll(clauses, literals)

      results.append(result)
    end = process_time() * 1000

    if np.all([result == True for result in results]):
      result = True
    elif np.all([result == False for result in results]):
      result = False

    print("[" + BASE + folder["name"] + "]", end = " ")
    print("instances:", str(limit), end = ", ")
    print("variables:", str(folder["variables"]), end = ", ")
    print("clauses:", str(folder["clauses"]), end = ", ")
    print("satisfiable:", str(folder["satisfiable"]), end = ", ")
    print("cpu_time:", format(end - start, ".3f"), "ms", end = ", ")
    print("result:", "OK" if result == folder["satisfiable"] else "ERROR")
