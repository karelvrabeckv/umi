# Module bt

"""
Solve a SAT with BACKTRACKING.
"""
def bt(clauses, literals):
  return run(clauses, literals, set())

def run(clauses, literals, model):
  # All clauses were POSITIVELY evaluated
  if not len(clauses):
    return True
  
  # Some clause was NEGATIVELY evaluated
  if any([not c for c in clauses]):
    return False

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
