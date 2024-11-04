number = input()
array = [0] * 10
answer = ''

for n in number:
    array[int(n)] += 1

for i in range(len(array)-1, -1, -1):
    if array[i] != 0:
        for _ in range(array[i]):
            answer += str(i)

print(int(answer))
