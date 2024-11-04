from itertools import combinations


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    count = (factorial(m)) / (factorial(m-n) * factorial(n))
    print(int(count))
