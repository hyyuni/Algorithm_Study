# 로봇 청소기
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
n, m = map(int, input().split())
r, c, d = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

visited[r][c] = 1 # 청소기 지점에서 시작
cnt = 1
while True:
    flag = 0 # 4 방향 확인
    for _ in range(4):  # 4방향 탐색
        d = (d+3) % 4   # 뱡향 전환 # 방향 0, 1, 2, 3  왼쪽으로 돌리면 3, 2, 1, 0
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                r = nr
                c = nc
                flag = 1
                break
    if flag == 0:
        # 네 방향 모두 청소를 할 수 없을 때
        if mat[r-dr[d]][c-dc[d]] == 1: # 후진 했을 때 벽이면 break
            print(cnt)
            break
        else: # 만약 뒤가 벽이 아니라면  후진한 위치로 갱신
            r, c = r-dr[d], c-dc[d]