# 피보나치 수열
# a(n) = a(n-1) + a(n-2), a(1) = 1, a(2) = 1
# f(4)를 구하는 과정 : f(3) + f(2) = (f(2) + f(1)) + f(2)
# 재귀함수 사용
def fibo_recursive(x):
    if x == 1 or x == 2:
        return 1
    return fibo_recursive(x-1) + fibo_recursive(x-2)

# 지수 시간 복잡도를 가져서 수행 시간이 많이 듦

# 피보나치 수열의 경우 - [최적 부분 구조, 중복되는 부분 문제] 조건 만족


# NOTE 하향식 구현 방식(메모이제이션) : 한번 계산한 결과를 메모리 공간에 메모
# 값을 기록해놨다가 재사용 : 캐싱(Caching)
# 탑다운 방식 사용
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
dp = [0] * 100


def fibo_dp(x):
    if x == 1 or x == 2:
        return 1
    # 이미 해결된 문제인 지 확인하는 부분
    if dp[x] != 0:
        return dp[x]
    # dp 테이블에 결과 저장
    dp[x] = fibo_dp(x-1) + fibo_dp(x-2)

    return dp[x]


# NOTE 상향식 구현 방식 : 반복문 사용해서 DP 테이블에 결과 저장
# 결과 저장용 리스트(DP 테이블) 사용
# 보텀업 방식 사용
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

# NOTE DP 접근방식
# DP 유형으로 풀 수 있는지 파악
# 그리디, 구현, 완전 탐색 등의 아이디어로 해결할 수 있는지 검토
# 시간 복잡도 해결이 안될 경우, 알고리즘 특성을 파악해서 DP 고려

# 예제 1 : 개미 전사
# 최소한 한 칸 이상 떨어진 식량 창고를 약탈하도록 고르기
# ai = i번째 식량창고까지의 최적의 해
# ki = i번째 식량창고에 있는 식량의 양
# 점화식 : ai = max(a(i-1), a(i-2)+ki)
n = int(input())
array = list(map(int, input().split()))
d = [0] * 100
# 보텀업 방식으로 해결
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])
print(d[n-1])

# 예제 2 : 1로 만들기
# 정수 X가 특정 연산을 거쳐 1이 될 때까지 수행되는 연산의 최솟값을 출력
# 점화식 : ai = min(a(i-1), a(i/2), a(i/3), a(i/5)) + 1

x = int(input())
d = [0] * 30001

for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1

    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)
print(d[x])

# 예제 3 : 효율적인 화폐 구성
# N가지 종류의 화폐가 있을 때, M원을 만들기 위한 최소한의 화폐 개수
# ai : 금액 i를 만들 수 있는 최소한의 화폐 개수
# k : 각 화폐의 단위
# 점화식 : 각 화폐 단위인 k를 하나씩 확인하며
# a(i-k)를 만드는 방법이 존재하는 경우, ai = min(ai, a(i-k)+1)
# a(i-k)를 만드는 방법이 존재하지 않는 경우, ai = INF

n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

d = [10001] * (m+1)
d[0] = 0
for i in range(n):  # 각 화폐
    for j in range(array[i], m+1):  # 각 금액
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

# 예제 4 : 금광
# n x m 크기의 금광에 각 칸마다 특정 크기의 금이 있음
# 첫 번째 열의 특정 행에서 출발하여 m-1번 이동하면서 얻을 수 있는 금의 최대 크기
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for _ in range(n):
        dp.append(array[index:index+m])
        index += m
    # DP 진행
    for i in range(1, m):  # 열기준 오른쪽으로 이동
        for j in range(n):
            # 왼쪽 위
            if j == 0:  # list 인덱스 범위 검사
                left_up = 0
            else:
                left_up = dp[j-1][i-1]
            # 왼쪽 아래
            if j == n-1:  # list 인덱스 범위 검사
                left_down = 0
            else:
                left_down = dp[j+1][i-1]
            # 왼쪽
            left = dp[j][i-1]
            dp[i][j] = dp[i][j] + max(left, left_down, left_up)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)

# 예제 5 : 병사 배치하기
# 전투력이 높은 병사가 앞쪽에 오도록 내림차순 배치
# 열외시키는 방법으로 배치하고, 남아 있는 병사의 수가 최대가 되도록
# LIS(가장 긴 증가하는 부분 수열)와 동일한 아이디어 -> 여기선 감소하는 부분 수열 구함
# d[i] : array[i]를 마지막 원소로 가지는 "부분 수열의 최대 길이"
# 점화식 : d[i] = max(d[i], d[j]+1)
n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
