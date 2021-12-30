# Module dpll

import numpy as np

"""
Solve a SAT with DPLL.
"""
def dpll(clauses, literals):
  global purity
  purity = set_purity(clauses, literals)

  return run(clauses, literals, set())

def run(clauses, literals, model):
  # All clauses were POSITIVELY evaluated
  if not len(clauses):
    return True
  
  # Some clause was NEGATIVELY evaluated
  if any([not c for c in clauses]):
    return False

  # Pure variables
  literal, val = find_pure_literal()
  if literal:
    cls = [c for c in clauses if (literal, val) not in c]
    rest = [l for l in literals if l != literal]
    mod = {*model, (literal, val)}
    return run(cls, rest, mod)

  # Unit propagation
  literal, val = find_unit_clause(clauses)
  if literal:
    cls = [c for c in clauses if (literal, val) not in c]
    cls = [c.difference({(literal, not val)}) for c in cls]
    rest = [l for l in literals if l != literal]
    mod = {*model, (literal, val)}
    return run(cls, rest, mod)

  # Select a literal
  literal, rest = literals[0], literals[1:]

  # Evaluate the literal POSITIVELY
  cls_pos = [c for c in clauses if (literal, True) not in c]
  cls_pos = [c.difference({(literal, False)}) for c in cls_pos]
  mod_pos = {*model, (literal, True)}

  # Evaluate the literal NEGATIVELY
  cls_neg = [c for c in clauses if (literal, False) not in c]
  cls_neg = [c.difference({(literal, True)}) for c in cls_neg]
  mod_neg = {*model, (literal, False)}

  return run(cls_pos, rest, mod_pos) or run(cls_neg, rest, mod_neg)

def set_purity(clauses, literals):
  purity = []
  for l in literals:
    occurences = []
    for c in clauses:
      occurences += [var[1] for var in c if var[0] == l]

    if np.all([val == True for val in occurences]):
      purity.append((l, True))
    elif np.all([val == False for val in occurences]):
      purity.append((l, False))
  return purity

def find_pure_literal():
  return purity.pop() if purity else (0, False)

def find_unit_clause(clauses):
  for c in clauses:
    if len(c) == 1:
      return list(c).pop()
  return (0, False)
