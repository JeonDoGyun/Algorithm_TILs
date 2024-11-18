import sys

n, m = map(int, sys.stdin.readline().strip().split())
package = []
per = []
count = 0

for _ in range(m):
    lines = list(map(int, sys.stdin.readline().strip().split()))
    package.append(lines[0])
    package.append(lines[1]*6)
    per.append(lines[1])

min_package = min(package)
min_per = min(per)

while n >= 0:
    if n >= 6:
        n -= 6
        count += min_package
    else:
        count += min(min_package, min_per * n)
        break


print(count)
