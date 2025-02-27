# 사각형 찾기
# 1. DFS로 1 찾기
# 2. 1의 개수 cnt
# 3. 최대값 찾기
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    global max_value, cnt
    visited[r][c] = 1
    cnt += 1

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if nr < 0  or nr >= n or nc < 0 or nc >= n:
            continue
        if visited[nr][nc] == 1:
            continue
        if graph[nr][nc]==1:
            dfs(nr, nc)
        max_value = max(cnt, max_value)
    return max_value


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    max_value = 0
    cnt = 0
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j] == 1:
                cnt = 0
                dfs(i, j)

    print(f'#{tc} {max_value}')