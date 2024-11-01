n = int(input())
array = []

for _ in range(n):
    array.append(list(input()))

start = array[0]
for i in range(1, len(array)):
    for j in range(len(start)):
        if start[j] != array[i][j]:
            start[j] = '?'


print(''.join(start))
