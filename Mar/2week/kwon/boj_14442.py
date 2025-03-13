# 벽 부수고 이동하기 2

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c, dist, broken):
    q = deque()
    q.append((r, c, dist, broken))  # (행, 열, 이동 거리, 벽 부순 횟수)

    # visited 3차원 리스트 (n행, m열, 벽 부순 횟수 K+1)
    visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1  # (0,0) 시작

    while q:
        r, c, dist, broken = q.popleft()

        # 도착점에 도달하면 거리 반환
        if r == n - 1 and c == m - 1:
            return dist

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            # 범위 벗어나면 무시
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            # 벽을 만났고, 부술 수 있는 경우
            if graph[nr][nc] == 1 and broken < k and visited[nr][nc][broken + 1] == 0:
                visited[nr][nc][broken + 1] = 1
                q.append((nr, nc, dist + 1, broken + 1))

            # 벽이 아니고, 방문한 적이 없는 경우
            elif graph[nr][nc] == 0 and visited[nr][nc][broken] == 0:
                visited[nr][nc][broken] = 1
                q.append((nr, nc, dist + 1, broken))

    return -1  # 도달 불가능할 경우 -1 반환


# 입력
n, m, k = map(int, input().split())  # n : 행 m : 열 k : 벽 부술 수 있는 횟수
graph = [list(map(int, input().strip())) for _ in range(n)]

print(bfs(0, 0, 1, 0))
