T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, cnt, K):
    global res

    if cnt > res:
        res = cnt
    visited[r][c] = 1

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            if arr[nr][nc] < arr[r][c]:
                dfs(nr, nc, cnt+1, K)
            elif arr[nr][nc] - K < arr[r][c]:
                copy_arr = arr[nr][nc]
                arr[nr][nc] = arr[r][c] - 1
                dfs(nr, nc, cnt+1, 0)
                arr[nr][nc] = copy_arr
    visited[r][c] = 0
    pass



for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_arr = 0
    res = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_arr:
                max_arr = arr[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_arr:
                dfs(i, j, 1, K)

    print(f'#{tc} {res}')