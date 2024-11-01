count = int(input())
array = list(map(int, input().split()))
array = sorted(array)

if len(array) == 1:
    print(pow(array[0], 2))
else:
    print(array[0]*array[-1])
