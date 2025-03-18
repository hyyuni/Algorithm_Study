from collections import deque
def brek_ice():
    global year
    q = deque()
    visited = [[0]*M for _ in range(N)]
    ans = 0 
    for i in range(1,N-1):
        for j in range(1,M-1):
            if glacier[i][j] > 0 and visited[i][j] == 0:
                sr,sc = i,j
                q.append((sr,sc))
                visited[sr][sc] = 1
                while q:
                    r,c = q.popleft()
                    cnt = 0
                    for dir in range(4):
                        nr = r + dr[dir]
                        nc = c + dc[dir]
                        if glacier[nr][nc] > 0 and visited[nr][nc]==0:
                            visited[nr][nc] = 1
                            q.append((nr,nc))
                        elif glacier[nr][nc] == 0 and visited[nr][nc]==0:
                            cnt += 1
                    if glacier[r][c] > cnt:
                        glacier[r][c] -= cnt
                    else:
                        glacier[r][c] = 0
                ans += 1
                # print(ans)
                for v in visited:
                    print(v)
                    print()
    if ans >= 2:
        return year
    elif ans == 1:
        year += 1
        return brek_ice()
    elif ans == 0:
        return -1

    


N , M = map(int,input().split())
glacier = [list(map(int,input().split())) for _ in range(N)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
year = 0
print(brek_ice())