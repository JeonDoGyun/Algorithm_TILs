import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

array = sorted(array, key=lambda x: (x[1], x[0]))

for i, j in array:
    print(i, j)
