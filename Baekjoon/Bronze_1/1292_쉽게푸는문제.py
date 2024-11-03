a, b = map(int, input().split())
array = []

for i in range(1, b+1):
    for j in range(0, i):
        array.append(i)

start = sum(array[:a-1])
end = sum(array[:b])

print(end - start)
