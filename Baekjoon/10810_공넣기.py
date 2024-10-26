n, m = map(int, input().split())
array = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())  # i부터 j까지 k번 공을 넣기
    # i-1번부터 j-1번까지 k값으로 바꾸기
    for a in range(i-1, j):
        array[a] = k

for i in array:
    print(i, end=' ')
