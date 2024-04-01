# 시간 초과 발생
# 이중 For문에서 단일 For문으로 변경하는 방식 고려

import sys
t = int(sys.stdin.readline())

for _ in range(t):
  n = int(input())
  rnk = []

  for _ in range(n):
    a,b = map(int, input().split())
    rnk.append([a, b])

  rnk = sorted(rnk, key=lambda x: x[0])
  count = 1
  man = rnk[0][1]

  for i in range(1, n):
    if rnk[i][1] < man:
      man = rnk[i][1]
      count += 1
        
  print(count)