import sys
from collections import deque

n = int(sys.stdin.readline())
array = deque()

for _ in range(n):
    action = list(sys.stdin.readline().split())
    match action[0]:
        case 'push':
            array.append(action[1])
        case 'pop':
            if len(array) == 0:
                print(-1)
            else:
                print(array.popleft())
        case 'size':
            print(len(array))
        case 'empty':
            if len(array) == 0:
                print(1)
            else:
                print(0)
        case 'front':
            if len(array) == 0:
                print(-1)
            else:
                print(array[0])
        case 'back':
            if len(array) == 0:
                print(-1)
            else:
                print(array[-1])
