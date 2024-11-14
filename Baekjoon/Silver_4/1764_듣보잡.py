import sys

n, m = map(int, sys.stdin.readline().split())
n_list = set()
m_list = set()

for _ in range(n):
    n_list.add(input())

for _ in range(m):
    m_list.add(input())

answer = sorted(list(n_list & m_list))

print(len(answer))
for a in answer:
    print(a)
