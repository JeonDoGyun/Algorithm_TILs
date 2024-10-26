n, m = map(int, input().split())
array = [i+1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())  # i, j 공 교환
    array[i-1], array[j-1] = array[j-1], array[i-1]

for i in array:
    print(i, end=' ')
