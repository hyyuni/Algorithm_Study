T = int(input())

for tc in range(1, T + 1):
    answer = 1 
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):
        i_set = set()
        j_set = set()
        for j in range(9):
            i_set.add(sudoku[i][j])
            j_set.add(sudoku[j][i])
        
        if len(i_set) != 9 or len(j_set) != 9:
            answer = 0
            break  

    if answer == 1:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                su9check = set()
                for k in range(3):
                    for l in range(3):
                        su9check.add(sudoku[i + k][j + l])
                
                if len(su9check) != 9:
                    answer = 0
                    break
            if answer == 0:
                break

    print(f'#{tc} {answer}')