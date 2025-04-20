from collections import deque
import heapq
from pprint import pprint

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(sy, sx):
    visited.add((sy,sx))
    q = deque([(sy,sx)])
    graph[sy][sx] = island_num
    edges = []

    while q:
        cy, cx = q.popleft()
        for dir in range(4):
            ny = cy + dy[dir]
            nx = cx + dx[dir]
            if not (0<=ny<n and 0<=nx<m):
                continue
            if graph[ny][nx] and (ny,nx) not in visited:
                visited.add((ny, nx))
                graph[ny][nx] = island_num
                q.append((ny, nx))
            elif not graph[ny][nx] and (cy,cx) not in edges:
                edges.append((cy, cx))
            
    return edges

def prim():
    visited = [False] * N
    hq = [(0,0)] # cost, node
    total = 0
    cnt = 0
    min_edge = [INF] * N

    while hq:
        cost, u = heapq.heappop(hq)

        if visited[u]:
            continue

        visited[u] = True
        total += cost
        cnt += 1

        for v in range(N):
            if not visited[v] and dist[u][v] < min_edge[v]:
                min_edge[v] = dist[u][v]
                heapq.heappush(hq, (dist[u][v], v))
    
    # 섬에 다리를 다 놨다면,
    if cnt == N:
        return total
    else:
        return -1 # 다리 놓기가 불가능 했다면,

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

# 섬 번호 매기기 & 경계값 구하기
visited = set()
island_edges = dict()
island_num = 1

for y in range(n):
    for x in range(m):
        if (y, x) not in visited and graph[y][x]:
            edges = bfs(y,x)
            island_edges[island_num] = edges
            island_num += 1

N = island_num - 1
INF = float('inf')
dist = [[INF]*N for _ in range(N)]

for num in range(1, island_num):
    for cy, cx in island_edges[num]:
        for dir in range(4):
            ny = cy + dy[dir]
            nx = cx + dx[dir]
            length = 0

            while 0<=ny<n and 0<=nx<m:
                
                if graph[ny][nx] == num:
                    break

                if graph[ny][nx]:
                    if length >= 2: # 다리 길이가 최소 2이상을 만족해야 하므로,
                        other_island = graph[ny][nx] -1 # 연결 됐다는 의미로 값을 -1 해주기
                        dist[num-1][other_island] = min(dist[num-1][other_island], length)
                    break
                ny += dy[dir]
                nx += dx[dir]
                length += 1

ans = prim()
print(ans)