import sys

n, m = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * 100001
dp[1] = array[0]

for i in range(1, len(array)):
    dp[i+1] = array[i] + dp[i]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(dp[j]-dp[i-1])
