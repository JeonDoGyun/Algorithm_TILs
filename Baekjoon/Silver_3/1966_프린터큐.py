import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    array = deque(map(int, sys.stdin.readline().split()))
    index = deque(i for i in range(n))  # index 관련 queue를 만들어서 같이 돌려주는게 포인트
    count = 0

    while True:
        if array[0] == max(array):
            count += 1

            if index[0] == m:
                print(count)
                break
            else:
                array.popleft()
                index.popleft()
        else:
            array.append(array.popleft())
            index.append(index.popleft())
