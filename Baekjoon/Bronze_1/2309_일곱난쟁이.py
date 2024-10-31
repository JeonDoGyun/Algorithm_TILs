from itertools import combinations

max_height = 100
array = []

for _ in range(9):
    array.append(int(input()))

answer = []
for combination in list(combinations(array, 7)):
    if sum(combination) == 100:
        answer = sorted(combination)
        break

for i in answer:
    print(i)
