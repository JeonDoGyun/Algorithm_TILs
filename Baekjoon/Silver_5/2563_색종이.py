n = int(input())
array = [[0] * 100 for _ in range(100)]
answer = 0

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            array[i][j] = 1

for i in range(100):
    answer += array[i].count(1)

print(answer)
