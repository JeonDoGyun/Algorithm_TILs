import sys
from collections import deque

n = int(sys.stdin.readline())
array = deque()

for _ in range(n):
    action = list(sys.stdin.readline().split())
    match action[0]:
        case 'push_front':
            array.appendleft(action[1])
        case 'push_back':
            array.append(action[1])
        case 'pop_front':
            if len(array) == 0:
                print(-1)
            else:
                print(array.popleft())
        case 'pop_back':
            if len(array) == 0:
                print(-1)
            else:
                print(array.pop())
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
