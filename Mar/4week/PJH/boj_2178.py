# from collections import deque
def bfs(si,sj):
    q = []
    q.append((si,sj))
    visited[si][sj] = 1

    while q:
        r,c = q.pop(0)
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or maze[nr][nc]==0:
                continue
            if visited[nr][nc] == 0:
                q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1
dr = [-1,1,0,0]
dc = [0,0,-1,1]
N, M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
bfs(0,0)
print(visited[N-1][M-1])
