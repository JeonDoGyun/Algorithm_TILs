from collections import deque
import sys

n = int(sys.stdin.readline().strip())
v = int(sys.stdin.readline().strip())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(v):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a] += [b]
    graph[b] += [a]


# def dfs(v):
#     visited[v] = True
#     for nx in graph[v]:
#         if not visited[nx]:
#             dfs(nx)


# dfs(1)

# print(visited.count(True)-1)

# bfs 방법 생각하기

visited[1] = 1
q = deque([1])

while q:
    num = q.popleft()
    for nx in graph[num]:
        if not visited[nx]:
            q.append(nx)
            visited[nx] = True

print(visited.count(True)-1)
