def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    while q:
        i,j = q.popleft()
        for dir in range(4):
            for t in range(wall_a[i][j]):
                ni = i + dr[dir]*t
                nj = j + dc[dir]*t
                if ni<0 or ni>=H or nj<0 or nj>=W or wall_a[ni][nj] == 0:
                    continue
                if wall_a[ni][nj]!=0:
                    q.append((ni,nj))
        wall_a[i][j] = 0                    
#벽돌 떨어뜨리기
# def wall_drip():
#     for j in range(W):
#         cnt = 0
#         wall_z = []
#         for i in range(H):
#             if wall_a[i][j] >= 1:
#                 cnt += 1
#                 wall_z.append(wall[i][j])
#         a = 0
#         for i in range(H-cnt,H):
#             wall_a[i][j] = wall_z[a]
#             a += 1
#         for i in range(0,H-cnt):
#             wall_a[i][j] = 0
def drop(graph):
    for x in range(W):
        # 현재 열에서 0이 아닌 벽돌만 stack에 저장
        stack = []
        for y in range(H):
            if graph[y][x] > 0:
                stack.append(graph[y][x])
        # 아래부터 stack에서 뽑아 차례로 채우고 나머지 0으로 채우기
        for y in range(H-1, -1, -1):
            if stack:
                graph[y][x] = stack.pop()
            else:
                graph[y][x] = 0
dr = [-1,1,0,0]
dc = [0,0,-1,1]
from collections import deque
from itertools import product
import copy
T = int(input())
for tc in range(1,T+1):
    N,W,H = map(int,input().split()) #N개의 구슬, H 행 W 열
    wall = [list(map(int,input().split())) for _ in range(H)]
    min_v = float('inf')
    for p in product(list(range(W)),repeat=N):
        wall_a = copy.deepcopy(wall)
        for j in p:
            for i in range(H):
                if wall_a[i][j] > 0:
                    bfs(i,j)
                    drop(wall_a)
                    break
        ans = 0
        for i in range(H):
            for j in range(W):
                if wall_a[i][j] != 0:
                    ans += 1
        min_v = min(min_v,ans)
    print(f'#{tc} {min_v}')


