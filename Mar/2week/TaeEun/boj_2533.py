import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# dp[node][0]: node가 얼리 어답터가 아닐 때, 최소 얼리 어답터 수
# dp[node][1]: node가 얼리 어답터일 때, 최소 얼리 어답터 수
dp = [[0, 0] for _ in range(N+1)]

stack = deque()
visited= [False]*(N+1)
stack.append((1, 0))

while stack:
    node, parent = stack.pop()
    if visited[node]:
        dp[node][0] = 0      # node가 얼리 어답터가 아니면, 자식은 모두 얼리 어답터여야 함
        dp[node][1] = 1      # node가 얼리 어답터면, 자기 자신 1 포함
        for child in graph[node]:
            if child == parent:
                continue
            dp[node][0] += dp[child][1]
            dp[node][1] += min(dp[child][0], dp[child][1])
    else:
        visited[node] = True
        stack.append((node, parent))
        for child in graph[node]:
            if child == parent:
                continue
            stack.append((child, node))

print(min(dp[1][0], dp[1][1]))
