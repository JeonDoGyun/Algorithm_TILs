array = []
length = []
answer = ''

for i in range(5):
    s = input()
    length.append(len(s))
    array.append(s)

for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            answer += array[j][i]

print(answer)
