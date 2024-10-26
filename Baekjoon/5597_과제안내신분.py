array = [i+1 for i in range(30)]

for _ in range(28):
    k = int(input())
    if k in array:
        array.remove(k)

for i in array:
    print(i)
