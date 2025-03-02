# 행렬찾기

def find_mat(r, c):
    global cnt
    visited[r][c] = 1
    row_size = 0
    col_size = 0
    for k in range(r, n): # 행 크기 구하기
        if graph[k][c] == 0:
            break
        row_size += 1

    for t in range(c, n):
        if graph[r][t] == 0:
            break
        col_size += 1

    for i in range(r, r+row_size): # 방문 처리
        for j in range(c, c+col_size):
            visited[i][j] = 1

    if row_size*col_size != 0: # 행렬이 존재하면
        cnt +=1
        mat.append([row_size*col_size, row_size, col_size])

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    mat = []
    cnt = 0 # 행렬 개수

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and visited[i][j]==0:
                find_mat(i, j)

    mat.sort(key = lambda x:(x[0],x[1]))
    print(f'#{tc} {cnt}', end = ' ')
    for i in range(len(mat)):
        print(mat[i][1], mat[i][2], end = ' ')
    print()