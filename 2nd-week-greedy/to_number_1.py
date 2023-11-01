def solve(N, K):
  res = 0
  while N > 1:
    if N % K == 0:
      N /= K
    else: N -= 1
    res += 1
  return res