T = int(input())

def dfs(row) :
    global count
    if row == N :
        count += 1
        return

    for col in range(N) :
        if col in column or (row-col) in left_up_right_down or (row+col) in right_up_left_down:
            continue
        
        column.add(col)
        left_up_right_down.add(row-col)
        right_up_left_down.add(row+col)

        dfs(row +1)
        
        column.remove(col)
        left_up_right_down.remove(row-col)
        right_up_left_down.remove(row+col)

        


for test_case in range(1, T + 1):
    N = int(input())
    count = 0
    column = set()
    left_up_right_down = set()
    right_up_left_down = set()
    dfs(0)
    print(f"#{test_case} {count}")
