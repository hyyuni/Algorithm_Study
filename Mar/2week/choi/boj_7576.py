from collections import deque

def bfs(arr):
    q = deque()
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    res = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                q.append((i, j, cnt))
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and visited[nx][ny] == 0:
                arr[nx][ny] = 1
                visited[nx][ny] = 1
                q.append((nx, ny, cnt+1))

    return cnt




M, N = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = [list(map(int, input().split())) for _ in range(N)]
cnt_3 = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            cnt_3 += 1
if cnt_3 == 0:
    print(0)
else:        
    a = bfs(arr)
    cnt_2 = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt_2 += 1
    if cnt_2 > 0:
        print(-1)
    else:
        print(a)