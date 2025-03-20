# 효율적인 해킹
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)

    visited = [0] * (N+1)
    visited[start] = 1
    cnt = 1

    while q:
        node = q.popleft()
        for next_node in com[node]:
            if visited[next_node] == 1:
                continue
            visited[next_node] = 1
            q.append(next_node)
            cnt += 1
    return cnt

N, M = map(int, input().split())
com = [[] for _ in range(N+1)]
max_cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    com[b].append(a)

for i in range(1, N+1):
    cnt = bfs(i)
    if max_cnt < cnt:
        max_cnt = cnt
        result = [i]
    elif cnt == max_cnt:
        result.append(i)

# result.sort()
print(*sorted(result))