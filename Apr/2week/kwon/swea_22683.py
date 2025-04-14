# 나무 베기
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y, end_x, end_y, k):
    q = deque()
    start_dir = 0  # 전진 방향(위쪽)

    visited[start_y][start_x][start_dir][0] = 1  # 시작방향:0, cnt = 0 상태로 시작
    q.append((start_x, start_y, start_dir, 0, 0))

    while q:
        x, y, dir, cut, cnt = q.popleft()

        if (x, y) == (end_x, end_y):
            return cnt

        # 현재 방향에서 전진
        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0 <= nx < n and 0 <= ny < n:
            if (graph[ny][nx] == 'G' or graph[ny][nx] == 'Y') and visited[ny][nx][dir][cut] == 0:
                visited[ny][nx][dir][cut] = 1
                q.append((nx, ny, dir, cut, cnt + 1))
            elif graph[ny][nx] == 'T' and cut < k and visited[ny][nx][dir][cut + 1] == 0:
                visited[ny][nx][dir][cut + 1] = 1
                q.append((nx, ny, dir, cut+1, cnt+1))

        # 좌회전
        left = (dir + 3) % 4
        if visited[y][x][left][cut] == 0:
            visited[y][x][left][cut] = 1
            q.append((x, y, left, cut, cnt+1))

        # 우회전
        right = (dir + 1) % 4
        if visited[y][x][right][cut] == 0:
            visited[y][x][right][cut] = 1
            q.append((x, y, right, cut, cnt+1))

    return -1

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    graph = [list(map(str, input())) for _ in range(n)]
    visited = [[[[0] * (k + 1) for _ in range(4)] for _ in range(n)] for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                start_x, start_y = j, i
            if graph[i][j] == 'Y':
                end_x, end_y = j, i
    ans = bfs(start_x, start_y, end_x, end_y, k)
    print(f'#{tc} {ans}')


