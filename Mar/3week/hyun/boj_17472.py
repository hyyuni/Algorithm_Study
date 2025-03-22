from collections import deque
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sy, sx):
    queue = deque([(sy, sx)])
    v.add((sy,sx))
    islands[sy][sx] = number

    while queue:
        cy, cx = queue.popleft()
        for dir in range(4):
            ny = cy + dy[dir]
            nx = cx + dx[dir]
            if not (0 <= ny < n and 0 <= nx < m):
                continue
            if islands[ny][nx] and (ny,nx) not in v:
                islands[ny][nx] = number
                v.add((ny,nx))
                queue.append((ny, nx))

def prim():
    visited = [False] * N
    hq = [(0, 0)]
    total_cost = 0
    cnt = 0
    min_edge = [INF] * N

    while hq:
        cost, u = heapq.heappop(hq)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost
        cnt += 1

        for v in range(N):
            if not visited[v] and graph[u][v] < min_edge[v]:
                min_edge[v] = graph[u][v]
                heapq.heappush(hq, (graph[u][v], v))

    if cnt == N:
        return total_cost
    else:
        return -1

n, m = map(int, input().split())
islands = [list(map(int, input().split())) for _ in range(n)]

# 섬 번호 매기기
number = 1
v = set()
for y in range(n):
    for x in range(m):
        if (y,x) not in v and islands[y][x] == 1:
            bfs(y, x)
            number += 1

N = number - 1  # 섬 개수
INF = float('inf')
graph = [[INF] * N for _ in range(N)]

# 섬 간 거리 계산 및 인접 행렬 생성
for y in range(n):
    for x in range(m):
        if islands[y][x] > 0:
            island_num = islands[y][x] - 1  # 현재 섬 번호 (0부터 시작)
            for dir in range(4):
                ny, nx = y + dy[dir], x + dx[dir]
                length = 0
                
                while 0 <= ny < n and 0 <= nx < m:
                    if islands[ny][nx] == island_num + 1:  # 같은 섬이면 중단
                        break
                    if islands[ny][nx] > 0:  # 다른 섬 발견
                        if length >= 2:
                            other = islands[ny][nx] - 1
                            graph[island_num][other] = min(graph[island_num][other], length)
                        break
                    ny += dy[dir]
                    nx += dx[dir]
                    length += 1

ans = prim()
print(ans)
