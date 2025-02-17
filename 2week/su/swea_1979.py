# 어디에 단어가 들어갈 수 있을까
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("swea_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

# 모든 칸을 완전탐색하려고 한다.
# 값이 1인 경우, 우/하 방향으로 탐색한다. (우/하를 동시에 하는 경우 네모칸 형태로 탐색하게 되니깐 따로 탐색해야 함에 주의)
    # 중복 탐색 제외
        # 왼쪽 칸 값이 1인 경우, 이미 가로방향 탐색했음
        # 위쪽 칸 값이 1인 경우, 이미 세로방향 탐색했음
# 탐색 구현
    # 탐색 함수
        # 현재 좌표와 방향을 파라미터로 받는다.
        # 다음 좌표가 0인 경우(벽), 중지한다. 
        # 낱말칸 길이를 리턴한다. 
from collections import defaultdict

T = int(input())
padded_arr = []

def get_len(pos, direction):
    cnt = 1 # 현재 글자칸도 유효함으로 0이 아닌 1로 시작해야 한다.
    r, c = pos
    dr, dc = direction
    while True:
        nr, nc = r + dr, c + dc
        if padded_arr[nr][nc] == 0: # 추가 테두리 감쌌으므로 범위 벗어나는 경우까지 고려되었음.
            return cnt
        cnt += 1
        r, c = nr, nc

for test_case in range(1, T + 1):
    N, K = map(int, input().split()) # 가로세로길이, 목표 단어 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    padded_arr = [[0] * (N+2) for _ in range(N+2)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            padded_arr[i][j] = arr[i-1][j-1]
    
    answer = 0
    info = defaultdict(int)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if padded_arr[i][j] == 0:
                continue

            directions = [] 
            right, down = (0, 1), (1, 0)
            pre_row, pre_col = i-1, j-1
            if padded_arr[pre_row][j] == 0:
                directions.append(down)
            if padded_arr[i][pre_col] == 0:
                directions.append(right)
            
            for d in directions:
                cell_len = get_len((i, j), d)
                info[cell_len] += 1

    print(f"#{test_case} {info[K]}")