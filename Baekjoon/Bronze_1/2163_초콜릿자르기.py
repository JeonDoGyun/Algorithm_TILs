n, m = map(int, input().split())
count = 0

if n < m:
    count = n-1 + n*(m-1)
else:
    count = m-1 + m*(n-1)

print(count)
