A = [0] * 20
B = [1] * 20
def check_col_k(film):
    cnt_streak = 0

    for col in range(W):
        cnt_0, cnt_1 = 0, 0
        
        for row in range(D):

            if film[row][col] == 0:
                cnt_0 += 1
                cnt_1 = 0  # 0이 나왔으므로 1의 연속은 끊김
            elif film[row][col] == 1:
                cnt_1 += 1
                cnt_0 = 0
            
            if cnt_0 >= K or cnt_1 >= K:
                cnt_streak += 1
                break  # 바로 다음 칼럼 보기. 
    
    return cnt_streak == W


def select_row(row, depth, film):  # dfs
    global answer

    if depth >= answer:
        return

    # 만약에 세로 칼럼 k가 모두 특정 문자열인 경우 답안 리턴하기
    if check_col_k(film):
        answer = min(answer, depth)
        return    
    
    
    for r in range(row + 1, D): 
        backup_row = film[r] 
        film[r] = A
        select_row(r, depth + 1, film)
        film[r] = B
        select_row(r, depth + 1, film)
        film[r] = backup_row
        

T = int(input())

for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    answer = K
    
    origin = [list(map(int, input().split())) for _ in range(D)]  
    if K == 1:
        print(f"#{tc} 0")
        continue
    
    if check_col_k(origin):
        print(f"#{tc} 0")
        continue

    select_row(-1, 0, origin)

    print(f"#{tc} {answer}")