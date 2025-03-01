import sys
sys.stdin = open("swea_input.txt", "r")
input = sys.stdin.readline

def print_snail(snail):
    for row in snail:
        print(*row)

T = int(input())

for t in range(1, T+1):
    N = int(input())

    snail = [[0] * N for _ in range(N)]

    # 방향: 우하좌상
    dr = [0, 1, 0, -1] 
    dc = [1, 0, -1, 0]  

    r, c, direction = 0, 0, 0

    for num in range(1, N*N + 1):
        snail[r][c] = num
        nr, nc = r + dr[direction], c + dc[direction] 
        print(nr, nc)
        if not (0 <= nr < N and 0 <= nc < N and snail[nr][nc] == 0):
            direction = (direction + 1) % 4  # 올바른 방향으로 변경
            nr, nc = r + dr[direction], c + dc[direction] # 다음 좌표값 재설정

        r, c = nr, nc # 이동


    print(f"#{t}")
    print_snail(snail)
