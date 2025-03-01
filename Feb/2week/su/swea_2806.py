# N-Queen
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("swea_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

# T = 10
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    answer = 0
    board = [[0] * N for _ in range(N)]
    
    def play(row, board):
        global answer
        if row == N:
            answer += 1
            return
        def is_valid(row, col, board):
            for i in range(row):  # 현재까지 놓인 퀸들에 대해 검사
                if board[i][col] == 1:  # 같은 열에 퀸이 있으면 안 됨
                    return False
                if row - col == i - board[i].index(1):  # 왼쪽 위 오른쪽 아래 대각선
                    return False
                if row + col == i + board[i].index(1):  # 왼쪽 아래 오른쪽 위 대각선
                    return False
            return True

        for col in range(N):
            if is_valid(row, col, board):
                board[row][col] = 1
                play(row + 1, board)
                board[row][col] = 0
    
    play(0, board)
        
    print(f"#{test_case} {answer}")