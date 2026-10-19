def Z(a, b):
  if b == 0:
    return 0
  return a + Z(a, b - 1)
