case = int(input())

for i in range(case):
    n = list(map(int, input().split()))
    avg = sum(n[1:])/n[0]
    count = 0
    for j in n[1:]:
        if j > avg:
            count += 1
    rate = count/n[0]*100
    print(f'{rate:.3f}%')
