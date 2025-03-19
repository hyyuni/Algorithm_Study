# # 등산로 조성
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(start_r, start_c, graph):
    q = deque()
    q.append((start_r, start_c, 1))
    max_depth = 1

    while q:
        r, c, depth = q.popleft()
        max_depth = max(max_depth, depth)

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if 0 <= nr < N and 0 <= nc < N and graph[r][c] > graph[nr][nc]:
                q.append((nr, nc, depth+1))

    return max_depth

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # K : 최대 깎을 수 있는 높이
    graph = [list(map(int, input().split())) for _ in range(N)]

    # visited = [[0] * N for _ in range(N)]
    max_length = 0
    max_height = 0
    max_height_pos = []

    for i in range(N):
        max_height = max(max_height, max(graph[i]))

    for i in range(N):
        for j in range(N):
            if graph[i][j] == max_height:
                max_height_pos.append((i, j)) # 최고 높이 봉우리 좌표 저장

    for height in max_height_pos:
        i, j = height

        for x in range(N):
            for y in range(N):
                if (x, y) == (i, j):
                    continue
                for k in range(0, K+1): # 깎기
                    graph[x][y] -= k
                    max_length = max(max_length, bfs(i, j, graph))
                    graph[x][y] += k # 복원

    print(f'#{tc} {max_length}')

