from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if land[nx][ny] == 1:
                q.append((nx, ny))
                land[nx][ny] = 0
    return

T = int(input())
for tc in range(T):
    M, N, baechu = map(int, input().split())
    land = [[0] * M for _ in range(N)]
    for i in range(baechu):
        i, j = map(int, input().split())
        land[j][i] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1:
                bfs(i, j)
                cnt+= 1
    print(cnt)
    