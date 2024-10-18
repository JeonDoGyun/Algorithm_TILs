t = int(input())

for _ in range(t):
    number = int(input())
    a, b = 1, 0
    for _ in range(number):
        a, b = b, a+b
    print(a, b)
