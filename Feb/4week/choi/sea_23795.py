T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    cnt = 0
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r, c = i, j
                break
    for i in range(4):
        nr, nc = r + dr[i], c+dc[i]
        while 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 0:
                arr[nr][nc] = 3
            elif arr[nr][nc] == 1:
                break
            nr = nr + dr[i]
            nc = nc + dc[i]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                result += 1
    print(f'#{tc} {result}')