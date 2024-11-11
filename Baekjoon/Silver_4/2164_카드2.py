from collections import deque

n = int(input())
array = deque([i for i in range(1, n+1)])

while len(array) != 1:
    first = array.popleft()
    second = array.popleft()
    array.append(second)

print(array[0])
