def go(dx, dy, di, desert):
    global res, i, j
    if di == 3 and i == dx and j == dy:
        res = max(res, len(desert))
        return

    if 0 <= dx < N and 0 <= dy < N and arr[dx][dy] not in desert:
        desert.add(arr[dx][dy]) 
        nx, ny = dx + direction[di][0], dy + direction[di][1]

        go(nx, ny, di, desert)  

        if di < 3:  # 방향 전환
            di += 1
            nx, ny = dx + direction[di][0], dy + direction[di][1]
            go(nx, ny, di, desert)

        desert.remove(arr[dx][dy]) 

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    direction = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    res = -1
    for i in range(N - 2):
        for j in range(1, N - 1):
            go(i, j, 0, set())

    print(f'#{tc} {res}')
