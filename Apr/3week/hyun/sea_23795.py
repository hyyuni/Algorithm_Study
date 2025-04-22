T = int(input())

dy = [-1, 0, 1, 0] # 상우하좌
dx = [0, 1, 0, -1]

def bfs(y, x):
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        while 0<=ny<N and 0<=nx<N:
            if arr[ny][nx]:
                break
            if not arr[ny][nx]:
                arr[ny][nx] = 1
                ny += dy[dir]
                nx += dx[dir]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 괴물(2) 찾기
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                bfs(y, x)

    ans = sum(row.count(0) for row in arr)

    print(f'#{tc} {ans}')