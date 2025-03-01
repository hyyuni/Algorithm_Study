import sys
from itertools import combinations
# from collections import deque

input = sys.stdin.readline

# DFS은 모든 집의 거리를 계산한 후에 종료 즉 cnt ==len(home) 했지만
# BFS는 가장 가까운 치킨집(최소 조건)을 찾는 순간 그 집의 탐색이 종료되므로 더 효율적임

'''
BFS 탐색을 하니 시간초과 에러가 나서.. 그냥 안 쓰기로 함
'''
# def bfs(chick_comb):
#     total = 0 # 집-치킨 거리를 전부 더한 최솟값
#     for ho_x, ho_y in home:
#         # 방문 처리를 for문 안에서 해야 새로운 집에 대한 치킨거리를 구할 수 있음
#         visited = [[0] * n for _ in range(n)]
#         q = deque([(ho_x, ho_y, 0)]) # 집의 x,y 좌표와 거리를 튜플로 queue에 넣기
#         visited[ho_x][ho_y] = 1

#         while q:
#             x, y, dist = q.popleft()
#             if (x, y) in chick_comb:
#                 total += dist
#                 break # 가장 가까운 치킨집을 찾으면 더 탐색할 필요 없이 종료

#             # 델타 탐색, 강사님이 델타탐색 좌표는 dx, dy로 해야 실수를 줄인다고 하셨음
#             for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#                 nx, ny = x+dx, y+dy
#                 if 0<= nx < n and 0<= ny < n and visited[nx][ny] == 0:
#                     visited[nx][ny] = 1
#                     q.append((nx, ny, dist +1)) # 방문 처리 후 거리에 +1을 해주기
#     return total



n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# 최소값을 구해야 하므로 비교하는 값을 무한대로 설정해놈
ans = float('inf')
home = []
chick = []
distances = []

# 집과 치킨 리스트 채우기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chick.append((i, j))

# BFS를 쓰지 않고 집-치킨 거리 미리 계산하기
distances = [[abs(hx - cx) + abs(hy - cy) for cx, cy in chick] for hx, hy in home]


# 치킨의 m개의 조합에 대해 최소 거리 계산
for chick_comb in combinations(range(len(chick)), m):
    total = 0
    for dist in distances:
        total += min(dist[i] for i in chick_comb)
    ans = min(ans, total)

print(ans)