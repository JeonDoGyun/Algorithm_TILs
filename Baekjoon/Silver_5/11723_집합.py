import sys

m = int(sys.stdin.readline())
s = set()

for _ in range(m):
    input_data = list(sys.stdin.readline().split())
    action = input_data[0]
    if action == 'add':
        s.add(int(input_data[1]))
    elif action == 'remove':
        try:
            s.remove(int(input_data[1]))
        except:
            pass
    elif action == 'check':
        if int(input_data[1]) in s:
            print(1)
        else:
            print(0)
    elif action == 'toggle':
        if int(input_data[1]) in s:
            s.remove(int(input_data[1]))
        else:
            s.add(int(input_data[1]))
    elif action == 'all':
        s = set([i for i in range(1, 21)])
    else:
        s = set()
