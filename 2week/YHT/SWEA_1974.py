def a(board):
    def b(unit):
        return sorted(unit) == list(range(1, 10))
    
    for i in range(9):
        if not b(board[i]) or not b([board[j][i] for j in range(9)]):
            return 0
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not b([board[x][y] for x in range(i, i+3) for y in range(j, j+3)]):
                return 0
    
    return 1

T = int(input())
for t in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    print(f"#{t} {a(board)}")
