x, y = map(int, input().split())

array = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

if x != 1:
    for i in range(0, x-1):
        y += array[i]

answer = days[(y-1) % 7]
print(answer)
