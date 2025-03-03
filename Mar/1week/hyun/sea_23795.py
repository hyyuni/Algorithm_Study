T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2. 함수 호출해 괴물 뻗어나가기
def solve(sx, sy):
    for dr in range(4):
        nx, ny = sx + dx[dr], sy + dy[dr]
        while 0<=nx<N and 0<=ny<N:          
            if arr[nx][ny] == 1:
                break
            else:
                arr[nx][ny] = 1
                nx += dx[dr]
                ny += dy[dr]  
                

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. 괴물 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                solve(i, j)
    
    # 3. 함수 종료후 괴물이 닿지 않는 자리 계산
    ans = sum(row.count(0) for row in arr)

    print(f'#{tc} {ans}')