# Gravity
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AYZOEkza5qMDFARc

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("swea_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

T = int(input())
# boxes[i] 는 최소0, 최대100
for test_case in range(1, T + 1):
    N = int(input()) # len(boxes)
    boxes = list(map(int, input().split()))
    tallest = max(boxes)

    answer = 0

    for i in range(N-1):
        temp = 0
        for j in range(i, N):
            if boxes[j] >= boxes[i]:
                temp += 1
        answer = max(answer, N-i-temp)

    print(f"#{test_case} {answer}")