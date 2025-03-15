from collections import deque
from copy import deepcopy

T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def count_zero(arr):
    return sum(row.count(0) for row in arr)
def bfs(r, c, arr):
    q = deque()
    q.append((r, c, arr[r][c]))
    while q:
        r, c, brick_num = q.popleft()
        arr[r][c] = 0
        for i in range(4):
            for k in range(1, brick_num):
                nr = r + (dr[i] * k)
                nc = c + (dc[i] * k)
                if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] != 0:
                    q.append((nr, nc, arr[nr][nc]))
                    arr[nr][nc] = 0
def dfs(cnt, arr):
    global min_v

    if cnt >= N or count_zero(arr) == total:
        min_v = min(min_v, total - count_zero(arr))
        return

    for col in range(W):
        copy_arr = deepcopy(arr)
        row = 9999
        for ni in range(H):
            if copy_arr[ni][col] != 0:
                row = ni
                break 
        if row == 9999:
            continue

        bfs(row, col, copy_arr)
        for i in range(W):
            idx = H - 1
            for j in range(H - 1, -1, -1):
                if copy_arr[j][i]:
                    copy_arr[idx][i], copy_arr[j][i] = copy_arr[j][i], copy_arr[idx][i]
                    idx -= 1
            for j in range(idx, -1, -1):
                copy_arr[j][i] = 0
        dfs(cnt + 1, copy_arr)
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]

    total = W * H
    min_v = total

    dfs(0, arr)
    print(f'#{tc} {min_v}')