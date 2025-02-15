# 신뢰
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXSVc1TqEAYDFAQT

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("swea_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    input_line = list(input().strip().split())
    
    t = 0
    click_t = 1 # 스위치 클릭하는데 걸리는 시간

    times = {
        "O": 0, # 로봇 별 마지막 시간
        "B": 0
    }
    pos = {
        "O": 1,
        "B": 1
    }

    for i in range(1, len(input_line) - 1, 2): # 인덱스 처리
        robot, btn_pos = input_line[i], int(input_line[i+1])
        
        move_t = abs(pos[robot] - btn_pos) # 로봇이 이동하는데 걸리는 시간
        spended_t = times[robot] + move_t # 이 로봇이 마지막으로 이동완료했을 때의 시간 + 현재 스위치까지 이동하는데 걸리는 시간 합산해줌
        t = max(t, spended_t) + click_t 

        times[robot] = t # 이 로봇 시간 갱신
        pos[robot] = btn_pos # 이 로봇 위치 갱신

    print(f"#{test_case} {t}")