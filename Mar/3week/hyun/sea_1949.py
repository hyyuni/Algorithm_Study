import sys
sys.stdin = open('input.txt', 'r')

dy = [-1,1,0,0]
dx = [0,0,-1,1]

T = int(input())

def dfs(cy, cx, length, cut):
    global max_len
    max_len = max(max_len, length)

    for dir in range(4):
        ny = cy + dy[dir]
        nx = cx + dx[dir]
        if not (0 <= ny < N and 0 <= nx < N):
            continue
        if not v[ny][nx]:
            if graph[ny][nx] < graph[cy][cx]:
                v[ny][nx] = 1
                dfs(ny, nx, length+1, cut)
                v[ny][nx] = 0
            elif not cut and graph[ny][nx] - K < graph[cy][cx]:
                height = graph[ny][nx]
                graph[ny][nx] = graph[cy][cx] - 1 # 자른 건 이전보다 낮기만 하면 됨 
                v[ny][nx] = 1
                dfs(ny, nx, length+1, 1)
                v[ny][nx] = 0
                graph[ny][nx] = height

for tc in range(1, T+1):
    N, K = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    max_height = max(max(row) for row in graph)
    max_len = 0

    v = [[0]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if graph[y][x] == max_height:
                v[y][x] = 1
                dfs(y,x,1,0)
                v[y][x] = 0

    print(f'#{tc} {max_len}')