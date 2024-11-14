n = int(input())
array = dict()

for _ in range(n):
    book = input()
    if book in array:
        array[book] += 1
    else:
        array[book] = 1

name = ''
max_count = 0
for key, value in array.items():
    if max_count < value:
        max_count = value
        name = key
    elif max_count == value:
        if key < name:
            name = key

print(name)
