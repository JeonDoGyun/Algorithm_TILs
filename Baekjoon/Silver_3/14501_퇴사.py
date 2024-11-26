import sys

n = int(sys.stdin.readline().strip())
tp = [list(map(int, sys.stdin.readline().strip().split())) for i in range(n)]
dp = [0 for i in range(n+1)]

for i in range(n):
    for j in range(i+tp[i][0], n+1):
        if dp[j] < dp[i]+tp[i][1]:
            dp[j] = dp[i]+tp[i][1]

print(dp[-1])
