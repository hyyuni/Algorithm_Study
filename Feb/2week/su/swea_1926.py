# 문제이름
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("swea_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

T = 10
# T = int(input())
# 박수는 숫자당 최대 세번까지만 센다. 
N = int(input())

def clap(s): 
    li = list(s) 
    cnt = 0
    targets = ["3", "6", "9"]
    for l in li:
        if l in targets:
            cnt += 1
    return cnt

answer = []
for i in range(1, N+1):
    result = clap(str(i))
    if result == 0:
        answer.append(i)
    else:
        answer.append(result*"-")
    
print(*answer)