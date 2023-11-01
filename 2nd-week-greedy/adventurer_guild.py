def solve(N, list_of_fear):
  list_of_fear.sort()
  res = 0
  acc = 0 # accumulator
  for member_fear in list_of_fear:
    acc += 1 # add 1 member first
    if acc >= member_fear:
      res += 1
      acc = 0
  return res

# input
print(solve(5, [2, 3, 1, 2, 2]))