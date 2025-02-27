def x_find(r,c):
    cntx = 1
    arr[r][c] = 0
    for k in range(1, N-c):
        if 0<= c+k < N:
            if arr[r][c+k] == 0:
                return cntx
            else:
                cntx += 1
                arr[r][c+k] = 0
    return cntx
def y_find(r,c):
    cnty = 1
    arr[r][c] = 0
    for k in range(1, N-r):
        if 0<= r+k < N:
            if arr[r+k][c] == 0:
                return cnty
            else:
                cnty += 1
                arr[r+k][c] = 0
    return cnty
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                x = x_find(i,j) 
                y = y_find(i,j)
                yebi_result = (x * y)
                if yebi_result > result:
                    result = yebi_result
                x = 0
                y = 0
    print(f'#{tc} {result}')

