res = 0
hour = int(input())
for h in range(hour + 1):
  for m in range(60):
    for s in range(60):
      if '3' in str(h) + str(m) + str(s): res += 1
print(res)