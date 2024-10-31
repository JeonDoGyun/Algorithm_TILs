a, b = map(int, input().split())
div = []

for i in range(max(a, b), 0, -1):
    if (a % i == 0) & (b % i == 0):
        div.append(i)
        a //= i
        b //= i

answer_div = 1
answer_mul = 1

for i in div:
    answer_div *= i
print(answer_div)
print(answer_div*a*b)
