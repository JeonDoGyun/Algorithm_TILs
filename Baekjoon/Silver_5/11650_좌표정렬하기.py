import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(tuple(map(int, input().split())))

array = sorted(array)

for i, j in array:
    print(i, j)
