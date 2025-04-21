from collections import deque
from pprint import pprint
import sys

sys.stdin = open('input.txt', 'r')

dy = [-1,1,0,0]
dx = [0,0,-1,1]


def bfs(sy,sx):
    visited = [[[False]*2 for _ in range(M)] for _ in range(N)] # 벽 부수기 기록용
    q = deque([(sy,sx,0,1)])
    visited[sy][sx][0] = True

    while q:
        cy, cx, brk, cnt = q.popleft()
        
        if (cy,cx) == (N-1,M-1):
            return cnt

        for dir in range(4):
            ny = cy + dy[dir]
            nx = cx + dx[dir]

            if not (0<=ny<N and 0<=nx<M):
                continue

            if not graph[ny][nx] and not visited[ny][nx][brk]:
                visited[ny][nx][brk] = True
                q.append((ny, nx, brk, cnt+1))
            elif graph[ny][nx] and brk == 0 and not visited[ny][nx][1]:
                visited[ny][nx][1] = True
                q.append((ny, nx, 1, cnt+1))

    return -1


N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]
min_v = float('inf')

ans = bfs(0,0)

print(ans)