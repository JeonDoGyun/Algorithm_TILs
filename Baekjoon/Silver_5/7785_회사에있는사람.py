import sys

n = int(sys.stdin.readline())
array = dict()

for _ in range(n):
    name, isHere = sys.stdin.readline().split()
    if isHere == 'enter':
        array[name] = 1
    else:
        del array[name]

array = sorted(array.keys(), reverse=True)

for i in array:
    print(i)
