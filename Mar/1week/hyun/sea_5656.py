import sys
from collections import deque
from itertools import product
from copy import deepcopy

sys.stdin = open('input.txt', 'r')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(sy, sx, graph):
    q = deque([(sy, sx)])
    v = [[0] * W for _ in range(H)]
    v[sy][sx] = 1

    while q:
        cy, cx = q.popleft()
        power = graph[cy][cx]
        graph[cy][cx] = 0  # 벽돌을 부숨

        for dr in range(4):
            for p in range(1, power):
                ny = cy + dy[dr]*p
                nx = cx + dx[dr]*p
                if 0 <= ny < H and 0 <= nx < W and v[ny][nx] == 0:
                    if graph[ny][nx]: # 벽돌이 0이 아니면 
                        q.append((ny, nx))
                    v[ny][nx] = 1

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

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(H)]
    ans = float('inf')

    for pos in product(range(W), repeat=N): # 어떤 위치(줄을) 선택하는 지, 중복 순열로 구해야 함
        graph_t = deepcopy(graph)
        remain = 0

        for x in pos:
            for y in range(H):
                if graph_t[y][x]:
                    bfs(y, x, graph_t)
                    drop(graph_t)
                    break
          
        for arr in graph_t:
            for i in arr:
                if i > 0:
                    remain += 1

        ans = min(ans, remain)

        if ans == 0:
            break

    print(f"#{tc} {ans}")
