from collections import deque
INF = float('inf')

directions = [(-1,0), (0, 1), (1, 0), (0, -1)]
# 0 = 위, 1 = 오, 2 = 아래, 3 = 왼쪽
# index+1은 우회전 index-1은 좌회전전

def bfs(matrix, k):
    N = len(matrix)
    dir_x = 0
    start = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'X':
                start = (i, j)
                break
        if start:
            break
    sr, sc = start
    visited = [[[[INF] * (K+1) for _ in range(4)]for _ in range(N)]for _ in range(N)]

    cnt = 0
    q = deque()
    q.append((sr, sc, dir_x, k, cnt))
    visited[sr][sc][dir_x][k] = cnt

    while q:
        r, c, d, remain, cost = q.popleft()

        # 현재 위치가 목표 Y라면 => cost가 최소 조작 횟수
        if matrix[r][c] == 'Y':
            return cost

        # 이미 더 짧은 방법으로 방문한 상태면 스킵
        if cost > visited[r][c][d][remain]:
            continue

        # 좌회전
        nd = (d - 1) % 4
        ncost = cost + 1
        if ncost < visited[r][c][nd][remain]:
            visited[r][c][nd][remain] = ncost
            q.append((r, c, nd, remain, ncost))

        # 우회전
        nd = (d + 1) % 4
        ncost = cost + 1
        if ncost < visited[r][c][nd][remain]:
            visited[r][c][nd][remain] = ncost
            q.append((r, c, nd, remain, ncost))

        # 전진
        nr = r + directions[d][0]
        nc = c + directions[d][1]
        if 0 <= nr < N and 0 <= nc < N:  # 범위 안
            cell = matrix[nr][nc]
            ncost = cost + 1

            if cell in ('G', 'X', 'Y'):
                # 그냥 갈 수 있음
                if ncost < visited[nr][nc][d][remain]:
                    visited[nr][nc][d][remain] = ncost
                    q.append((nr, nc, d, remain, ncost))

            elif cell == 'T':
                # 나무가 있으면 남은 벌목 횟수가 있어야 통과 가능
                if remain > 0:
                    nremain = remain - 1
                    if ncost < visited[nr][nc][d][nremain]:
                        visited[nr][nc][d][nremain] = ncost
                        q.append((nr, nc, d, nremain, ncost))

    # 큐가 빌 때까지 Y를 찾지 못했다면 불가능
    return -1

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())  
    matrix = [input() for _ in range(N)]
    ans = bfs(matrix, K)
    print(f'#{tc}', ans)