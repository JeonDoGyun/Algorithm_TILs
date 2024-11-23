import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().strip().split())
array = [i for i in range(1, n+1)]
answer = list(permutations(array, m))

for i in answer:
    for j in i:
        print(j, end=' ')
    print()
