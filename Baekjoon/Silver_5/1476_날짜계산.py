answer = 1
e, s, m = map(int, input().split())

while True:
    if ((answer-e) % 15 == 0) and ((answer-s) % 28 == 0) and ((answer-m) % 19 == 0):
        break
    answer += 1

print(answer)
