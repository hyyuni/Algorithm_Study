# 미로1
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    q = deque()
    q.append((x, y))
    visited[y][x] =1

    while q:
        x, y = q.popleft()
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if ny < 0 or ny >=16 or graph[ny][nx] == 1 or visited[ny][nx] == 1:
                continue
            if graph[ny][nx] == 3:
                return 1
            visited[ny][nx] = 1
            q.append((nx, ny))

    return 0

for i in range(1, 11):
    T = int(input())
    graph = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    ans = dfs(1, 1)

    print(f'#{T} {ans}')