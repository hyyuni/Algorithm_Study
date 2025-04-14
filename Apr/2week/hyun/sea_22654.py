T = int(input())

# 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def delta(sy, sx, start, commands):
    y, x, dir = sy, sx, start
    n = len(field)

    for c in commands:
        if c == 'L':
            dir = (dir - 1) % 4
        elif c == 'R':
            dir = (dir + 1) % 4
        elif c == 'A':
            ny, nx = y + dy[dir], x + dx[dir]
            if 0 <= ny < n and 0 <= nx < n and field[ny][nx] != 'T':
                y, x = ny, nx

    return (y, x)

for tc in range(1, T + 1):
    N = int(input())
    field = [list(input()) for _ in range(N)]

    # X와 Y의 위치를 찾고 저장
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                sy, sx = i, j
            if field[i][j] == 'Y':
                ey, ex = i, j

    Q = int(input())
    ans = []

    for _ in range(Q):
        temp = input().split()
        C = int(temp[0])
        commands = temp[1]

        cy, cx = delta(sy, sx, 0, commands)

        # 이동한 위치가 목적지에 도달했는지 확인
        if (cy, cx) == (ey, ex):
            ans.append('1')
        else:
            ans.append('0')

    print(f'#{tc}', *ans)