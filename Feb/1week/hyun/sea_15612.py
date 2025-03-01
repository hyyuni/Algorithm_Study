T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(8)] # 8 X 8 크기의 체스판에 룩 입력
    row_rook = set() # 룩이 있는 행의 중복 체크, 순서가 각각 1개씩 들어가야 함
    column_rook = set() # 룩이 있는 열의 중복 체크
    rook_cnt = 0 # 룩의 개수 세기, 최종적으로 룩의 개수는 무조건 8개가 되야 함
    invalid = False # **잘못된 경우 루프를 탈출하는 Flag변수**

    for i in range(8):
        for j in range(8):
            if arr[i][j] == 'O':
                if i in row_rook or j in column_rook:
                    print(f'#{tc} no') # 행의 set이나 열의 set에 이미 i가 있다면 중복이므로
                    invalid = True # 잘못된 상태 표시
                    break # 반복문을 바로 빠져 나옴
              
 
                rook_cnt += 1 #룩의 개수를 더해주고
                row_rook.add(i) # 행 기록
                column_rook.add(j) # 열 기록
        if invalid: # 바깥쪽 루프도 빠져나가야 함, 빠져나오지 못하면 정답이 여러번 출력됨
            break
    if not invalid:              
        if rook_cnt == 8:
            print(f'#{tc} yes')
        else:
            print(f'#{tc} no')

