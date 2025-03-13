from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0, 1, 0))  # (행, 열, 이동 거리, 벽 부순 여부)
    
    # visited 3차원 리스트 (n행, m열, 벽 부순 여부 2가지)
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1  # (0,0) 시작

    while q:
        r, c, dist, broken = q.popleft()

        # 도착점에 도달하면 거리 반환
        if r == n - 1 and c == m - 1:
            return dist

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < n and 0 <= nc < m:
                # 벽이 아니고, 방문하지 않은 경우
                if graph[nr][nc] == 0 and visited[nr][nc][broken] == 0:
                    visited[nr][nc][broken] = 1
                    q.append((nr, nc, dist + 1, broken))

                # 벽이지만, 아직 벽을 부순 적이 없는 경우
                elif graph[nr][nc] == 1 and broken == 0 and visited[nr][nc][1] == 0:
                    visited[nr][nc][1] = 1  # 벽을 부순 상태로 방문 체크
                    q.append((nr, nc, dist + 1, 1))

    return -1  # 도달 불가능할 경우 -1 반환

# 입력
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

print(bfs())