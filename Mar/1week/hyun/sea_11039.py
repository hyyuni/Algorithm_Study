T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                x, y = 1, 1
                while j+x <N and arr[i][j+x] == 1:
                    x += 1
                while i+y < N and arr[i+y][j] == 1:
                    y += 1
                ans = max(ans, x*y)

    print(f'#{tc} {ans}')