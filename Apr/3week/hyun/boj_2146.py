from collections import deque
from pprint import pprint

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(sy, sx):
    visited.add((y,x))
    q = deque([(sy,sx)])
    graph[sy][sx] = island_num
    edges = []
    while q:
        for _ in range(len(q)):
            cy, cx = q.popleft()
            for dir in range(4):
                ny = cy + dy[dir]
                nx = cx + dx[dir]

                if not (0<=ny<N and 0<=nx<N):
                    continue

                if (ny, nx) not in visited and graph[ny][nx]:
                    visited.add((ny,nx))
                    graph[ny][nx] = island_num
                    q.append((ny,nx))
                
                elif not graph[ny][nx] and (cy,cx) not in edges:
                    edges.append((cy,cx))
    return edges

def bridge(edges, num):
    q = deque()
    dist = [[-1]*N for _ in range(N)]

    # 출발점 거리 = 0
    for y,x in edges:
        q.append((y, x))
        dist[y][x] += 1
    
    while q:
        cy, cx = q.popleft()

        for dir in range(4):
            ny = cy + dy[dir]
            nx = cx + dx[dir]

            if not (0<=ny<N and 0<=nx<N):
                continue
            
            # 다리를 놓다가 다른 섬을 만났을 때
            if graph[ny][nx] and graph[ny][nx] != num:
                return dist[cy][cx]

            # 바다에 다리를 놓아야 하는 경우
            if not graph[ny][nx] and dist[ny][nx] == -1:
                dist[ny][nx] = dist[cy][cx] + 1
                q.append((ny,nx))

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

# 번호매기기 + 경계값 구하기
visited = set()
island_num = 1
island_edges = dict()
for y in range(N):
    for x in range(N):
        if (y,x) not in visited and graph[y][x]:
            edges = bfs(y,x)
            island_edges[island_num] = edges
            island_num += 1


# pprint(graph)
# pprint(island_edges)

ans = float('inf')

for num in range(1, island_num):
    min_length = bridge(island_edges[num], num)
    ans = min(ans, min_length)

print(ans)