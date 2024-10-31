import sys

input = sys.stdin.readline
n = int(input())

# 새로운 정렬 알고리즘 생각 : 계수정렬 사용
array = [0] * 10001
for _ in range(n):
    array[int(input())] += 1

for i in range(len(array)):
    if array[i] != 0:
        for _ in range(array[i]):
            print(i)
