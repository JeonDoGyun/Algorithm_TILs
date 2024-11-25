import sys
from itertools import product

n, m = map(int, sys.stdin.readline().strip().split())
array = [i for i in range(1, n+1)]
answer = list(product(array, repeat=m))

for i in answer:
    for j in i:
        print(j, end=' ')
    print()
