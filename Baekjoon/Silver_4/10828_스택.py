import sys

n = int(sys.stdin.readline())
array = []

for i in range(n):
    action = sys.stdin.readline().split()

    if action[0] == 'push':
        array.append(action[1])
    elif action[0] == 'pop':
        if len(array) == 0:
            print(-1)
        else:
            print(array.pop())
    elif action[0] == 'size':
        print(len(array))
    elif action[0] == 'empty':
        if len(array) == 0:
            print(1)
        else:
            print(0)
    elif action[0] == 'top':
        if len(array) == 0:
            print(-1)
        else:
            print(array[-1])
