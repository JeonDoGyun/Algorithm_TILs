from collections import deque


def radix_sort(arr):
    queues = [deque() for _ in range(10)]  # 10개의 큐 생성

    max_num = max(arr)  # 최대값 찾기
    max_digit = len(str(max_num))  # 최대값의 자릿수

    exp = 1  # 자릿수
    for _ in range(max_digit):
        for num in arr:
            digit = (num // exp) % 10
            queues[digit].append(num)

        # 큐에 있는 값들을 다시 arr에 넣어줌
        idx = 0
        for queue in queues:
            while queue:
                arr[idx] = queue.popleft()
                idx += 1

        exp *= 10  # 자릿수 증가

    return arr
