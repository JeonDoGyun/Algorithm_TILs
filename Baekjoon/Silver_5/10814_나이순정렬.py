import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    age, name = input().split()
    array.append((int(age), name))
array = sorted(array, key=lambda x: x[0])

for a, b in array:
    print(a, b)
