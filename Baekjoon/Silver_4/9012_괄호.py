import sys

n = int(sys.stdin.readline())

for _ in range(n):
    ps = input()
    count = 0
    answer = 'YES'

    for i in range(len(ps)):
        if ps[i] == '(':
            count += 1
        elif ps[i] == ')':
            count -= 1

        if count < 0:
            answer = 'NO'

    if count != 0:
        answer = 'NO'

    print(answer)
