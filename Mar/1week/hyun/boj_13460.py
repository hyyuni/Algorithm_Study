from collections import deque

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
visited = []
rx = ry = bx = by = 0

# 델타 탐색을 위한 dx, dy 생성하기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 2. 이동함수
def solve(cx, cy, dx, dy):
    cnt = 0
    while graph[cx+dx][cy+dy] != '#' and graph[cx+dx][cy+dy] != '0':
            cx += dx
            cy += dy
            cnt +=1
            if graph[cx][cy] == 'O':
                break
    return cx, cy, cnt

# 3. BFS
def bfs(m, rx, ry, bx, by):
    q = deque()
    q.append((m,rx,ry,bx,by))
    visited.append((rx, ry, bx, by))

    while q:
        m, rx, ry, bx, by = q.popleft()
        if m > 10:
            break
        for i in range(4):
            r_mx, r_my, r_cnt = solve(rx, ry, dx[i], dy[i])
            b_mx, b_my, b_cnt = solve(bx, by, dx[i], dy[i])
        
            if graph[b_mx][b_my] == 'O':
                continue
            if graph[r_mx][r_my] == 'O':
                print(m)
                return
            if b_mx == r_mx and b_my == r_my:
                if r_cnt > b_cnt:
                    r_mx -= dx[i]
                    r_my -= dy[i]
                else:
                    b_mx -= dx[i]
                    b_my -= dy[i]

            if (r_mx, r_my, b_mx, b_my) not in visited:
                visited.append((r_mx, r_my, b_mx, b_my))
                q.append((m+1, r_mx, r_my, b_mx, b_my))
    print(-1)
                    
# 1. 구슬 저장하기
for x in range(N):
    for y in range(M):
        if graph[x][y] == 'R':
            rx, ry = x, y
        elif graph[x][y] == 'B':
            bx, by = x, y

bfs(1, rx, ry, bx, by)

