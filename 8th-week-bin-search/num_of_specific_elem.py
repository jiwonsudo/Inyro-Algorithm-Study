import bisect, sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

startIdx = bisect.bisect_left(num_list, n)
endIdx = bisect.bisect_right(num_list, m)

print(endIdx - startIdx)