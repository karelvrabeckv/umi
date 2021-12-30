# Module loader

"""
Load instance.
"""
def get_instance(path):
  with open(path) as f:
    lines = f.readlines()

  cnf = get_cnf(lines)
  clauses = get_clauses(cnf)
  literals = get_literals(clauses)

  return (clauses, literals)

"""
Load CNF.
"""
def get_cnf(lines):
  cnf = []
  for line in lines:
    data = line.split()

    # Avoid empty lines and
    # the lines that starts with
    # specified characters
    if not data or data[0] in {"c", "p", "%", "0"}:
      continue

    # Remove zeros from the lines
    data = [num for num in data if num != "0"]

    cnf.append(data)
  return cnf

"""
Load clauses.
"""
def get_clauses(lines):
  clauses = []
  for line in lines:
    clause = set()
    for num in line:
      literal = int(num)
      if literal < 0:
        clause.add((abs(literal), False))
      elif literal > 0:
        clause.add((literal, True))
    clauses.append(clause)
  return clauses

"""
Load literals.
"""
def get_literals(lines):
  literals = set()
  for line in lines:
    for num in line:
      literals.add(num[0])
  literals = list(literals)
  return literals
