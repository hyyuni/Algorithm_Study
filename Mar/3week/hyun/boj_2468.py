import sys
sys.setrecursionlimit(10**4)

dy = [-1,1,0,0]
dx = [0,0,-1,1]

# graph의 숫자가 h 높으면 안 잠겼으므로 해당 부분만 탐색
def dfs(cy, cx, h):
    visited[cy][cx] = 1
    for dir in range(4):
        ny = cy + dy[dir]
        nx = cx + dx[dir]
        if not (0<= ny< N and 0<=nx<N):
            continue
        if not visited[ny][nx] and graph[ny][nx] > h:
            dfs(ny, nx, h)

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

max_height = max(map(max, graph))
max_v = 1

for h in range(1, max_height):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if graph[y][x] > h and not visited[y][x]:
                dfs(y,x,h)
                cnt += 1
    if cnt == 0:
        break
    max_v = max(max_v, cnt)

print(max_v)