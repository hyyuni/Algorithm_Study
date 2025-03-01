import sys

from collections import defaultdict
from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().strip().split()) # 배추밭 가로길이, 세로 길이, 배추 위치 개수

    arr = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        col, row = map(int, sys.stdin.readline().strip().split())
        arr[row][col] = 1

    def bfs(s_row, s_col):
        global arr
        queue = deque()
        queue.append((s_row, s_col))
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        while queue:
            row, col = queue.popleft()
            for i in range(4):
                nr = dr[i] + row
                nc = dc[i] + col
                if nr < 0 or nc < 0 or nr >= N or nc >= M:
                    continue
                if arr[nr][nc] == 0:
                    continue

                arr[nr][nc] = 0
                queue.append((nr, nc))

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                count += 1
                arr[i][j] = 0
                bfs(i, j)
    print(count)