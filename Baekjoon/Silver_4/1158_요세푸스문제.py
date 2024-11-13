import sys

n, k = map(int, sys.stdin.readline().split())
array = [i for i in range(1, n+1)]

answer = []
new_k = 0

for i in range(n):
    new_k += k-1
    if new_k >= len(array):
        new_k %= len(array)
    answer.append(str(array.pop(new_k)))

print("<", ", ".join(answer), ">", sep="")
