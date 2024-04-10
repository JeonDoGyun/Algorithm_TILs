def solution(numbers, target):
    answer = 0
    graph = [0]
    
    for num in numbers:
        temp = []
        for i in graph:
            temp.append(i + num)
            temp.append(i - num)
        graph = temp
    
    for i in graph:
        if i == target:
            answer += 1
    
    return answer
  
# bfs로 풀기
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer