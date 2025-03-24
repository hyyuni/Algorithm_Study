#등산로 규칙
#1. 등산로는 가장 높은 봉우리에서 시작해야한다.
#2. 등산로는 높->낮 
#3. 딱 한곳, 최대 K 깊이만큼 지형을 깎을 수 잇음
def dfs(cnt,sr,sc,brek):        
    global max_cnt
    max_cnt = max(max_cnt,cnt)

    visited[brek][sr][sc] = 1
    # print(cnt)
    # print(mount[sr][sc])
    # for v in visited:
    #     print(v)
    for dir in range(4):
        nr = sr + dr[dir]
        nc = sc + dc[dir]
        if nr<0 or nr>=N or nc<0 or nc>=N:
            continue 
        if brek == 0:
            if mount[nr][nc] >= mount[sr][sc] and visited[brek][nr][nc] == 0:
                if mount[nr][nc]-mount[sr][sc] < K:
                    original = mount[nr][nc]
                    mount[nr][nc] = mount[sr][sc]-1
                    dfs(cnt+1,nr,nc,brek+1)
                    mount[nr][nc] = original
            elif mount[nr][nc] < mount[sr][sc] and visited[brek][nr][nc] == 0:
                dfs(cnt+1,nr,nc,brek)
        else:
            if mount[nr][nc] < mount[sr][sc] and visited[brek][nr][nc] == 0:
                dfs(cnt+1,nr,nc,brek)
    visited[brek][sr][sc] = 0
    
         




T = int(input())
dr = [-1,1,0,0]
dc = [0,0,-1,1]
for tc in range(1,T+1):
    N, K = map(int,input().split())
    mount = [list(map(int,input().split())) for _ in range(N)]
    visited = [[[0]*N for _ in range(N)] for _ in range(2)]
    height = []
    for m in mount:
        height += m
    max_v = max(list(set(height)))
    max_cnt = 0
    real_max = 0
    for i in range(N):
        for j in range(N):
            if mount[i][j] == max_v:
                dfs(1,i,j,0)
                real_max = max(max_cnt,real_max)
    print(f'#{tc} {real_max}')