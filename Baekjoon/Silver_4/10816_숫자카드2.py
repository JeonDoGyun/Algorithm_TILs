n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

array = [0] * 20000001
answer = []
for a in n_list:
    array[a+10000000] += 1

for b in m_list:
    answer.append(array[b+10000000])

for i in answer:
    print(i, end=' ')
