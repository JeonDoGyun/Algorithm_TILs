# n = int(input())
# n_list = list(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))

# array = [0] * 20000001
# answer = []
# for a in n_list:
#     array[a+10000000] += 1

# for b in m_list:
#     answer.append(array[b+10000000])

# for i in answer:
#     print(i, end=' ')

# 메모리 사용 줄이기 위해 dict() 사용하기
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

array = dict()
for a in n_list:
    if a in array:
        array[a] += 1
    else:
        array[a] = 1

for b in m_list:
    if b in array:
        print(array[b], end=' ')
    else:
        print(0, end=' ')
