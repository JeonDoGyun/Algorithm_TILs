# f(n-2) + f(n-3) = f(n)
# 시간 맞추기 위해 DP를 사용해야 됨

import sys
arr = [0, 1, 1, 1] + [0 for _ in range(97)]

def dp(x):
  if arr[x]:
    return arr[x]
  else:
    arr[x] = dp(x-2) + dp(x-3)
    return arr[x]

t = int(sys.stdin.readline())
for _ in range(t):
  n = int(sys.stdin.readline())
  print(dp(n))
