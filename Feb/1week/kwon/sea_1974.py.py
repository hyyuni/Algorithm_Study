# 스도쿠 검증
T = int(input())
for tc in range(1,T+1):
    mat = [list(map(int,input().split())) for _ in range(9)]

    for i in range(9):
        row = 0 # 행의 합
        column = 0
        row += sum(mat[i])
        for j in range(9):
            column += mat[i][j] # 열의 합
            if i%3 == 0 and j%3 == 0: # 3X3 합
                box = 0
                for i in range(3):
                    for j in range(3):
                        box += mat[i][j]
    if row == 45 and column == 45 and box == 45:
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')

    # set 이용 len(set) = 9