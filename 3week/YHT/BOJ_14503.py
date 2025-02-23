def a():
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    b = [list(map(int, input().split())) for _ in range(n)]

    c = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    e = 0

    while True:
        if b[x][y] == 0:
            b[x][y] = 2
            e += 1

        f = False
        for _ in range(4):
            d = (d + 3) % 4
            nx, ny = x + c[d][0], y + c[d][1]

            if b[nx][ny] == 0:
                x, y = nx, ny
                f = True
                break

        if not f:
            bd = (d + 2) % 4
            bx, by = x + c[bd][0], y + c[bd][1]

            if b[bx][by] != 1:
                x, y = bx, by
            else:
                break

    print(e)

a()
