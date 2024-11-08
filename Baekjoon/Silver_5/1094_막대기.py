# answer = [64]
# x = int(input())

# while True:
#     if sum(answer) == x:
#         break
#     l = answer.pop()
#     l //= 2
#     answer.append(l)
#     if sum(answer) < x:
#         answer.append(l)
#         if sum(answer) == x:
#             break

# print(len(answer))

# 조금 더 빠른 방법 생각 : 그리디 알고리즘으로 풀기
x = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(stick)):
    if x >= stick[i]:
        count += 1
        x -= stick[i]

    if x == 0:
        break

print(count)
