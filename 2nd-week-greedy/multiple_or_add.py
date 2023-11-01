def solve(S):
  res = 1
  S = S.replace('0', '') # Because it doesn't affect the calculation
  int_list_of_S = list(map(lambda word: int(word), list(S)))
  for num in int_list_of_S:
    if num == 1: res += 1
    else: res *= num
  return res