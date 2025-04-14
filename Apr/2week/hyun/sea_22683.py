from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(sy, sx, ey, ex):
    # 방문처리를 다차원 배열로 늘려 나무를 벤 횟수, 방향까지 체크해줘야 함
    visited = [[[[False] * (K+1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
    q = deque()

    # 시작 방향은 항상 위쪽(0)
    dir = 0
    visited[sy][sx][dir][0] = True
    q.append((sy, sx, dir, 0, 0))

    while q:
        y, x, dir, cut, cnt = q.popleft()

        if (y, x) == (ey, ex):
            return cnt

        # 전진
        ny, nx = y + dy[dir], x + dx[dir]
        if 0 <= ny < N and 0 <= nx < N:
            cell = field[ny][nx]
            if cell in ('G', 'Y') and not visited[ny][nx][dir][cut]:
                visited[ny][nx][dir][cut] = True
                q.append((ny, nx, dir, cut, cnt + 1))
            elif cell == 'T' and cut < K and not visited[ny][nx][dir][cut + 1]:
                visited[ny][nx][dir][cut + 1] = True
                q.append((ny, nx, dir, cut + 1, cnt + 1))

        # 좌회전
        ldir = (dir + 3) % 4
        if not visited[y][x][ldir][cut]:
            visited[y][x][ldir][cut] = True
            q.append((y, x, ldir, cut, cnt + 1))

        # 우회전
        rdir = (dir + 1) % 4
        if not visited[y][x][rdir][cut]:
            visited[y][x][rdir][cut] = True
            q.append((y, x, rdir, cut, cnt + 1))

    return -1

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    field = [list(input().strip()) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if field[y][x] == 'X':
                sy, sx = y, x
            if field[y][x] == 'Y':
                ey, ex = y, x

    ans = bfs(sy, sx, ey, ex)
    print(f'#{tc} {ans}')