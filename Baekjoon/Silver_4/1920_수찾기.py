# import sys

# input = sys.stdin.readline

# n = int(input())
# n_list = set(map(int, input().split()))

# m = int(input())
# m_list = list(map(int, input().split()))

# for a in m_list:
#     if a in n_list:
#         print(1)
#     else:
#         print(0)

# 문제에서 의도한 방식으로 풀기 : 이분 탐색 사용

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))


for a in m_list:
    left, right = 0, n-1
    isExist = False

    while left <= right:
        mid = (left+right) // 2
        if a == n_list[mid]:
            isExist = True
            print(1)
            break
        elif a > n_list[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if not isExist:
        print(0)
