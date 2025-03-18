from collections import deque
from copy import deepcopy

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def count_iceberg(graph):
    #빙산이 몇 개의 덩어리인지 확인하는 함수
    visited = [[0] * M for _ in range(N)]
    chunk_count = 0
    
    for y in range(N):
        for x in range(M):
            if graph[y][x] > 0 and visited[y][x] == 0:
                chunk_count += 1
                q = deque([(y, x)])
                visited[y][x] = 1
                
                while q:
                    cy, cx = q.popleft()
                    for dr in range(4):
                        ny, nx = cy + dy[dr], cx + dx[dr]
                        if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] > 0 and not visited[ny][nx]:
                            visited[ny][nx] = 1
                            q.append((ny, nx))
    
    return chunk_count

def melt_icebergs(graph):
    # 빙산을 녹이는 함수
    melted_graph = deepcopy(graph)
    for y in range(N):
        for x in range(M):
            if graph[y][x] > 0:
                sea_count = 0
                for dr in range(4):
                    ny, nx = y + dy[dr], x + dx[dr]
                    if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
                        sea_count += 1
                melted_graph[y][x] = max(0, graph[y][x] - sea_count)
    return melted_graph

# 입력 받기
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

year = 0

while True:
    iceberg_chunks = count_iceberg(graph)  # 빙산 덩어리 수 확인

    if iceberg_chunks >= 2:  
        print(year)  # 빙산이 두 덩어리 이상으로 분리된 첫 해 출력
        break
    elif iceberg_chunks == 0:  
        print(0)  # 빙산이 완전히 녹은 경우
        break

    graph = melt_icebergs(graph)  # 빙산 녹이기
    year += 1  # 연도 증가
