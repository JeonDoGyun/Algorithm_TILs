n, m = map(int, input().split())
n_list = set()
count = 0
for _ in range(n):
    n_list.add(input())

for _ in range(m):
    a = input()
    if a in n_list:
        count += 1

print(count)
