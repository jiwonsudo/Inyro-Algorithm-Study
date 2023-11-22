import sys

n, m = list(map(int, sys.stdin.readline().split()))
heights = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(heights)

res = 0
while (start <= end):
  total_cutted = 0
  point = (start + end) // 2
  for cutted in heights:
    if cutted > point:
      total_cutted += cutted - point
  if total_cutted < m:
    end = point - 1
  else:
    res = point
    start = point + 1

print(res)