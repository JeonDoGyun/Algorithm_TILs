from collections import deque

n, m = map(int, input().split())
target = list(map(int, input().split()))
queue = deque([i for i in range(1, n+1)])
count = 0

for num in target:  # 2 9 5
    while True:
        if queue[0] == num:
            queue.popleft()
            break
        else:
            # 왼쪽
            if queue.index(num) < (len(queue)/2):
                while queue[0] != num:
                    queue.append(queue.popleft())
                    count += 1
            # 오른쪽
            else:
                while queue[0] != num:
                    queue.appendleft(queue.pop())
                    count += 1
print(count)
