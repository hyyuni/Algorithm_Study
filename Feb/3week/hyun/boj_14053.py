# dir 북(0) 동(1) 남(2) 서(3)
# 왼쪽 회전? 0-> 3-> 2-> 1 = 즉 방향전환은 (dir+3)%4 부터 시작

def solve(cx, cy, dr):
    cnt = 0
    while True: # 청소기가 움직이지 못할 때까지 while문
        arr[cx][cy] = 2 # 청소처리
        cnt += 1

        flag = True # 플래그 변수로 while문 조정
        while flag:
            # 왼쪽부터 시작해 4방향 탐색하기 (미청소 영역 체크)
            for d in ((dr+3)%4, (dr+2)%4, (dr+1)%4, dr): # 3, 2, 1, 0
                nx, ny = cx + dx[d],  cy +dy[d]
                if arr[nx][ny] == 0:
                    cx, cy, dr = nx, ny, d
                    flag = False # flag를 변경해줘야 while문도 탈출이 가능함
                    break
            else: # 4방향 모두 미청소된 영역이 없으면 = 후진
                back_x, back_y = cx - dx[dr], cy - dy[dr]
                if arr[back_x][back_y] == 1: # 벽을 만났다면?
                    return cnt
                else:
                    cx, cy = back_x, back_y

# 북,동,남,서 변수
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
sx, sy, dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = solve(sx, sy, dr)
print(ans)