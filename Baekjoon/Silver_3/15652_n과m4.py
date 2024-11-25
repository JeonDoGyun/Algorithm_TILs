import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().strip().split())
array = [i for i in range(1, n+1)]
answer = list(combinations_with_replacement(array, m))

for i in answer:
    for j in i:
        print(j, end=' ')
    print()
