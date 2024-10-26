n, m = map(int, input().split())
array = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    array_slice = array[i-1:j]
    array_slice.reverse()
    array[i-1:j] = array_slice

for i in array:
    print(i, end=' ')
