# 연결 요소의 개수
import sys
sys.setrecursionlimit(2000)

def dfs(graph, v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for i  in range(1, N+1):
    if visited[i] == 0:
        dfs(graph, i)
        cnt += 1

print(cnt)