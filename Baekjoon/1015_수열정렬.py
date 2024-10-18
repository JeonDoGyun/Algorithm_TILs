n = int(input())
array = list(map(int, input().split()))
sorted_arr = sorted(array)
answer = []

for i in range(n):
    answer.append(sorted_arr.index(array[i]))
    sorted_arr[sorted_arr.index(array[i])] = -1

for i in range(n):
    print(answer[i], end=' ')
