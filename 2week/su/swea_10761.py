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
    btns_info = {
        "O": [],
        "B": []
    }
    btns_cnt = {
        "O": 0,
        "B": 0
    }
    for i in range(1, len(input_line) - 1, 2): # 인덱스 처리
        robot, btn_pos = input_line[i], int(input_line[i+1])
        btns_info[robot].append(btn_pos)
        btns_cnt[robot] += 1

    btns_info["O"].sort()
    btns_info["B"].sort()
 
    answer = -1
    for robot, btns in btns_info.items():
        if not btns: # 누를 버튼 없는 경우 예외처리
            longest = 0
        else:
            longest = btns[-1]
        times = longest + btns_cnt[robot]
        
        if times > answer:
            answer = times
    print(f"#{test_case} {answer}")
        
