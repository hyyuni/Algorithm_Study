from collections import deque

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        r, c = 0, j
        q = deque()
        while r < N:
            if not q and arr[r][c] == 1:
                q.append(1)
            elif q and arr[r][c] == 2:
                cnt += 1
                q.pop()
            r += 1
    print(f'#{tc} {cnt}')