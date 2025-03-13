# 벽돌 깨기
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def breaking_bricks(r, c, cnt):
    queue = deque()
    queue.append((r,c,cnt))
    k = graph[r][c]  # 구슬 닿은 벽돌의 숫자

    graph[r][c] = 0 # 구슬 닿은 벽돌 = 0
    visited[r][c] = 1 # 방문처리

    fill_blank() # 빈 공간 채우기

    while queue:
        r, c, cnt = queue.popleft()

        if cnt > n: # 공수를 초과하면 break
            return

        # k = graph[r][c] # 구슬이 닿은 벽돌 숫자
        for dir in range(4):
            for t in range(1, k+1):
                nr = r + dr[dir]*t
                nc = c + dc[dir]*t
                if nr < 0 or nr >= h or nc < 0 or nc >= w or graph[nr][nc] == 0 or visited[nr][nc] == 1:
                    continue

                # 벽돌 숫자만큼 벽돌 제거
                visited[nr][nc] = 1
                graph[nr][nc] = 0
                queue.append((nr, nc, cnt+1))
    return
                    # graph[nr-(k-1)][nc-{k-1}] = 0 # 벽돌 숫자 -1 만큼 상하좌우 벽돌 제거

def fill_blank():
    for j in range(h):
        for i in range(w):
            for k in range(1, h-j+1):
                if j+k < h:
                    if graph[j+k][i] != 0:
                        graph[j][i] = 1
                        graph[j+k][i] = 0
                    # 빈공간이 있을 경우 벽돌은 밑으로 !
                    # graph[r+1][c] != 0 위 칸이 0이 아닌 0의 위치 찾기
                    # graph[r][c] = 1 # 그 칸이 존재할 경우 해당 위치는 0
                    # graph[r+1][c] = 0
T = int(input())
for tc in range(1, T+1):
    n, w, h = map(int, input().split()) #  공 수, 가로, 세로 
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    ans = 0 

    breaking_bricks(0,0,1)

    for j in range(h):
        for i in range(w):
            if graph[j][i] > 0:
                ans += 1
    
    print(f'#{tc} {ans}')