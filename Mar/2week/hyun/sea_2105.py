'''
for i in range(idx, idx+2)를 통해 현재 방향 유지 또는 다음 방향으로 전환 두 가지 경우를 탐색
if ny == sy and nx == sx and i == 3 and cnt >=4: 정확히 네 번째 방향(마지막 방향)을 사용한 후,
출발점으로 돌아왔고 최소한 사각형(디저트가 최소 4개 이상)을 형성했을 때만 최대값을 갱신.
'''

import sys
sys.stdin = open('input.txt', 'r')

# 이동방향: 우하(0), 좌하(1), 좌상(2), 우상(3)
dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]

# 가능한 방향 전환 순서 (시작 방향에 따라 달라짐)
directions = [
    (0, 1, 2, 3),
    (1, 2, 3, 0),
    (2, 3, 0, 1),
    (3, 0, 1, 2)
]

def dfs(cy, cx, sy, sx, dr, idx, cnt):
    global max_v

    for i in range(idx, idx+2):  # 현재 방향 유지(idx), 또는 다음 방향(idx+1)으로 전환
        if i >= 4:
            continue
        ny = cy + dy[dr[i]]
        nx = cx + dx[dr[i]]

        if ny == sy and nx == sx and i == 3 and cnt >= 4:
            max_v = max(max_v, cnt)
            return

        if 0 <= ny < N and 0 <= nx < N and graph[ny][nx] not in visited:
            visited.add(graph[ny][nx])
            dfs(ny, nx, sy, sx, dr, i, cnt + 1)
            visited.remove(graph[ny][nx])

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    max_v = -1

    # 모든 좌표를 시작점으로 하여 탐색 진행
    for y in range(N):
        for x in range(N):
            for dr in directions:
                visited = set() # visited는 탐색마다 초기화해야 함
                visited.add(graph[y][x])
                dfs(y, x, y, x, dr, 0, 1)

    print(f'#{tc} {max_v}')