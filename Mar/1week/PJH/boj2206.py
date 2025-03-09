from collections import deque
import copy
N,M = map(int,input().split())
wall = [list(map(int,input())) for _ in range(N)]

brek = []
for i in range(N):
    for j in range(M):
        if wall[i][j] == 1:
            brek.append((i,j))
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def bfs(s,e):
    q = deque()
    q.append((s,e))
    visited[s][e] = 1
    while q:
        i,j = q.popleft()
        for d in range(4):
            ni = i+dr[d]
            nj = j+dc[d]
            if 0<=ni<N and 0<=nj<M and wall_a[ni][nj]==0 and visited[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    if visited[N-1][M-1]==0:
        return -1
    else:
        return visited[N-1][M-1]

# ans = 9999
# for b in brek:
#     visited = [[0]*M for _ in range(N)]
#     wall_a = copy.deepcopy(wall)
#     r,c = b
#     wall_a[r][c] = 0
#     bfs(0,0)
#     if visited[N-1][M-1]!=0:
#         ans = min(ans,visited[N-1][M-1])
#
# if ans == 9999:
#     print(-1)
# else:
#     print(ans)




