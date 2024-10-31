t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    A = a
    B = b
    n = 1
    while n != 0:
        n = A % B
        A = B
        B = n

    print(int(a*b/A))
