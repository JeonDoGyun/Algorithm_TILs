import sys

n = int(sys.stdin.readline())
n_array = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_array = list(map(int, sys.stdin.readline().split()))
n_array.sort()


# 시간을 절약시킬 수 있는 탐색법 고려 : 이분 탐색 사용

def binary_search(num):
    l = 0
    r = n - 1
    while l <= r:
        mid = (l+r) // 2
        if n_array[mid] == num:
            return 1
        elif n_array[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
    return 0


for i in m_array:
    print(binary_search(i), end=' ')
