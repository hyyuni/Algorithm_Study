from collections import deque
 
dx = [-1, -1, -1, 1, 1, 1, 0, 0] # 방향 탐색
dy = [-1, 0, 1, -1, 0, 1, -1, 1]
 
def count_mines(x, y):
    cnt = 0
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '*':
            cnt += 1
    return cnt
 
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] =1
 
    while queue:
        x, y = queue.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == '.':
                visited[nx][ny] = 1
                if mine_count[nx][ny] == 0:
                    queue.append((nx, ny))
 
def count_clicks():
    click_cnt = 0
 
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '.':
                mine_count[i][j] = count_mines(i, j)
 
    for i in range(n):
        for j in range(n):
            if mine_count[i][j] == 0 and graph[i][j] == '.' and not visited[i][j]:
                bfs(i, j)
                click_cnt += 1
 
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '.' and not visited[i][j]:
                click_cnt +=1 
    return click_cnt
 
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    graph = [list(map(str, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    mine_count = [[0] * n for _ in range(n)]
 
    print(f'#{tc} {count_clicks()}')