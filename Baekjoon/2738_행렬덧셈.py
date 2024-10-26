n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))

answer = []
for i in range(n):
    array = []
    for j in range(m):
        array.append(a[i][j]+b[i][j])
    answer.append(array)

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()
