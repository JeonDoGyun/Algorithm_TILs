base = [1, 1, 2, 2, 2, 8]
array = list(map(int, input().split()))  # 0 1 2 2 2 7
answer = []
for i in range(len(array)):
    answer.append(base[i] - array[i])

for i in answer:
    print(i, end=' ')
