import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(sy, sx):
    q = deque([(sy,sx)])
    v.add((sy,sx))
    graph[sy][sx] = island_num
    edge = []  # 이 섬의 경계 좌표들
    while q:
        cy, cx = q.popleft()
        
        for dir in range(4):
            ny = cy + dy[dir]
            nx = cx + dx[dir]

            if not (0<=ny<N and 0<=nx<N):
                continue
            if (ny,nx) not in v and graph[ny][nx] == 1:
                graph[ny][nx] = island_num
                v.add((ny,nx))
                q.append((ny,nx))
            elif graph[ny][nx] == 0 and (cy,cx) not in edge:
                edge.append((cy,cx))

    return edge

def bridge(edge, island_num):
    q = deque()
    dist = [[-1]*N for _ in range(N)] # dist를 +1 씩 증가하는 방문 리스트와 같이 사용
    
    for y,x in edge:
        q.append((y,x))
        dist[y][x] = 0

    while q:
        cy,cx = q.popleft()

        for dir in range(4):
            ny = cy + dy[dir]
            nx = cx + dx[dir]

            if not (0<=ny<N and 0<=nx<N):
                continue
            
            # 다른 섬을 만났다면 거리 반환
            if graph[ny][nx] != 0 and graph[ny][nx] != island_num:
                return dist[cy][cx]

            # 바다이고 아직 방문하지 않았다면 확장
            if graph[ny][nx] == 0 and dist[ny][nx]==-1:
                dist[ny][nx] = dist[cy][cx]+1
                q.append((ny,nx))

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 섬 번호 매기기, 섬의 경계 저장하기
island_num = 1
v = set()
island_edges = dict() # Key: 섬번호, Value: 경계 저장 딕셔너리

for y in range(N):
    for x in range(N):
        if (y,x) not in v and graph[y][x]:
            edges = bfs(y, x)
            island_edges[island_num] = edges
            island_num += 1

ans = float('inf')

for i in range(1, island_num):
    lenth = bridge(island_edges[i], i)
    ans = min(ans, lenth)

print(ans)