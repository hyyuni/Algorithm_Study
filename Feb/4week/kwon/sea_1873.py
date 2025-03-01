# 상호의 배틀필드
T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    game = [list(input()) for _ in range(H)]
    n = int(input())
    user = list(input())

    # 전차 위치 찾기
    x, y = -1, -1
    for i in range(H):
        for j in range(W):
            if game[i][j] in ['<', '>', '^', 'v']:
                x, y = j, i
                break

    for a in user:
        if a == 'U':
            game[y][x] = '^'
            if y-1 >= 0 and game[y-1][x] == '.':
                game[y-1][x] = '^'
                game[y][x] = '.'
                y -= 1

        elif a == 'D':
            game[y][x] = 'v'
            if y+1 < H and game[y+1][x] == '.':
                game[y+1][x] = 'v'
                game[y][x] = '.'
                y += 1

        elif a == 'R':
            game[y][x] = '>'
            if x+1 < W and game[y][x+1] == '.':
                game[y][x+1] = '>'
                game[y][x] = '.'
                x += 1

        elif a == 'L':
            game[y][x] = '<'
            if x-1 >= 0 and game[y][x-1] == '.':
                game[y][x-1] = '<'
                game[y][x] = '.'
                x -= 1

        elif a == 'S':
            if game[y][x] == '>':
                for k in range(x+1, W):
                    if game[y][k] == '#':
                        break
                    if game[y][k] == '*':
                        game[y][k] = '.'
                        break

            elif game[y][x] == '<':
                for k in range(x-1, -1, -1):
                    if game[y][k] == '#':
                        break
                    if game[y][k] == '*':
                        game[y][k] = '.'
                        break

            elif game[y][x] == '^':
                for k in range(y-1, -1, -1):
                    if game[k][x] == '#':
                        break
                    if game[k][x] == '*':
                        game[k][x] = '.'
                        break

            elif game[y][x] == 'v':
                for k in range(y+1, H):
                    if game[k][x] == '#':
                        break
                    if game[k][x] == '*':
                        game[k][x] = '.'
                        break

    print(f'#{tc}', end=' ')
    for i in range(H):
        print(''.join(game[i]))