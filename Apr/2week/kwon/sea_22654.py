# 차윤이의 RC카
dy = [-1, 0, 1, 0] # 0 : 상 1 : 우 2 : 하 3 : 좌
dx = [0, 1, 0, -1]

def RC(start_x, start_y, end_x, end_y, commands):
    x, y = start_x, start_y
    dir = 0

    for cmd in commands:
        if cmd == 'A':
            ny = y + dy[dir]
            nx = x + dx[dir]

            if 0 <= nx < N and 0 <= ny < N and field[ny][nx] != 'T':
                x, y = nx, ny

        elif cmd == 'L':
            dir =  (dir + 3) % 4

        elif cmd == 'R':
            dir = (dir + 1) % 4

    if (x, y) == (end_x, end_y):
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(str, input())) for _ in range(N)]
    Q = int(input())
    ans = []
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                start_x, start_y = j, i
            if field[i][j] == 'Y':
                end_x, end_y = j, i

    for i in range(Q):
        C, command = input().split()
        c = int(C)
        commands = list(command)

        result = RC(start_x, start_y, end_x, end_y, commands)
        ans.append(result)

    print(f'#{tc}', end = ' ')
    print(*ans)
