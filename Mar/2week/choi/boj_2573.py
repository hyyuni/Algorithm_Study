from collections import deque
def melt(arr):
    global melt_count
    melt_count += 1
    visited = [[0] * M for _ in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j] != 0:
                cnt = 0
                visited[i][j] = 1
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                        cnt += 1
                arr[i][j] = arr[i][j] - cnt 
                if arr[i][j] < 0 :
                    arr[i][j] = 0  
    


def iceblock_count(arr):
    global cnt
    q = deque()
    visited_iceblock = [[0] * M for _ in range(N)]
    ans = 0
    cnt = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            cnt += arr[i][j]
            if arr[i][j] != 0 and visited_iceblock[i][j] == 0:
                q.append((i, j))
                visited_iceblock[i][j] = 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if arr[nx][ny] != 0 and visited_iceblock[nx][ny] == 0:
                            q.append((nx, ny))
                            visited_iceblock[nx][ny] = 1
                ans += 1
    if cnt == 0:
        return 0
    return ans

                
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
melt_count = 0
cnt = 0
while True:
    res = iceblock_count(arr)
    if cnt == 0:
        print(0)
        break
    if res >= 2:
        print(melt_count)
        break
    else:
        melt(arr)
