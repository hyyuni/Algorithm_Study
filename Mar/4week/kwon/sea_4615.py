# 재미있는 오셀로 게임
dx = [-1, 1, -1, -1, 1, 1, 0, 0]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def put(b_arr, w_arr):
    for i in range(len(b_arr)):
        x, y = b_arr[i]
        chess[y][x] = 1
    for i in range(len(w_arr)):
        x, y = w_arr[i]
        chess[y][x] = 2
            
def dfs(x, y, color):
    chess[y][x] = color 
    
    for dir in range(8):
        nx = x + dx[dir]
        ny = y + dy[dir]
        flip = [] # 뒤집을 돌 리스트 
        
        while 0<= nx < N and 0 <= ny < N and chess[ny][nx] != 0:
            if chess[ny][nx] == color: # 자기 색 만나면 뒤집기
                for fx, fy in flip:
                    chess[fy][fx] = color
                break
            else:
                flip.append((nx, ny)) # 다른 색 만나면 뒤집을 리스트에 추가
            nx = nx + dx[dir]
            ny = ny + dy[dir]       
                     
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    chess = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    b_pos = [(N//2 -1, N//2), (N//2, N//2 -1)]
    w_pos = [(N//2 - 1, N//2 - 1), (N//2,N//2)]
    black = 0 # 흑돌 개수 cnt
    white = 0 # 백돌 개수 cnt
    
    put(b_pos, w_pos) # 초기 돌 놓기

    for _ in range(M):
        x, y, c = map(int, input().split())
        if c == 1:
            b_pos.append((x-1, y-1))
        else:
            w_pos.append((x-1, y-1))

        dfs(x-1, y-1, c)
    
    
    for y in range(N):
        for x in range(N):
            if chess[y][x] == 1:
                black += 1
            elif chess[y][x] == 2:
                white += 1
            
    print(f'#{tc} {black} {white}')
