# n = int(input())
# count = 0

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)


# for i in str(factorial(n))[::-1]:
#     if i != '0':
#         break
#     count += 1

# print(count)

# 더 효율적인 방법 : n에서 5로 나눠 떨어지는 수가 몇개인지 찾기 ex_ 10 : 5, 10 | 2개
n = int(input())
count = 0

while n != 0:
    n //= 5
    count += 1

print(count)
