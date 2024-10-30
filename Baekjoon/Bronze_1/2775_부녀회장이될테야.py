test = int(input())

for _ in range(test):
    k = int(input())
    n = int(input())
    k0 = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            k0[j] += k0[j-1]

    print(k0[-1])
