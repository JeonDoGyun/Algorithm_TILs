import sys

n, m = map(int, sys.stdin.readline().strip().split())
passwords = {}

for _ in range(n):
    domain, password = map(str, sys.stdin.readline().strip().split())
    passwords[domain] = password

for _ in range(m):
    domain = sys.stdin.readline().strip()
    print(passwords[domain])
