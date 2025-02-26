T = int(input())

def direction(sx, sy):
    global dr
    if arr[sx][sy] == '^':
        dr = 0
    elif arr[sx][sy] == 'v':
        dr = 1
    elif arr[sx][sy] == '<':
        dr = 2
    elif arr[sx][sy] == '>':
        dr = 3

def direction2(i):
    global dr
    if i == 'U':
        dr = 0
    elif i == 'D':
        dr = 1
    elif i == 'L':
        dr = 2
    elif i == 'R':
        dr = 3

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]
dr = 0
# 방향 전환 할 때 이동 후, 탱크의 방향을 바꿔줘야 하므로 리스트에 저장하기
tank = ['^', 'v', '<', '>']

for tc in range(1, T+1):
    # 높이 H, 너비 W
    H, W = map(int, input().split())
    # 게임 격자판
    arr = [list(input()) for _ in range(H)]
    # 게임 입력
    N = int(input())
    control = input()
    # 전차 시작 변수 초기화
    sx = sy = -1
    
    # 1. 게임을 시작하기 위해 2차원배열에서 전차 찾기 (^, v, <, >)
    flag = False
    for i in range(H):
        for j in range(W):
            if arr[i][j] in tank:
                sx, sy = i, j
                direction(sx, sy)
                flag = True
                break
        if flag:
            break

    for i in control:
        if i == 'S':
            nx, ny = sx, sy
            while True:
                nx += dx[dr]
                ny += dy[dr]
                if not (0 <= nx < H and 0 <= ny < W):
                    break
                if arr[nx][ny] == '#':
                    break
                elif arr[nx][ny] == '*':
                    arr[nx][ny] = '.'
                    break
            
        elif i in ['U', 'D', 'L', 'R']:
            direction2(i)
            arr[sx][sy] = tank[dr] # '#'을 만나 이동을 못했더라도 방향을 바꿔야 함
            nx = sx + dx[dr]
            ny = sy + dy[dr]
            if 0<= nx < H and 0 <= ny < W and arr[nx][ny] == '.':
                arr[sx][sy] = '.' # 지나간 자리 평탄화
                sx, sy = nx, ny
                arr[sx][sy] = tank[dr] # 이동후 탱크 방향 수정하기

    print(f'#{tc}', end = " ")
    for row in arr:
        print(''.join(row))