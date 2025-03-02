# 스위치 조작
# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AZHA7Cn6ZgsDFAQP

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("swea_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

N = -1
T = int(input())

def toggled(arr, idx):
    for i in range(idx, N):
        arr[i] = (arr[i] + 1) % 2
    return arr

for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    answer = 0

    # 0~N-1까지 모든 요소들을 확인하면서
    # 다른 게 나오는 순간 토글시킨다.
    # 토글시키는 함수는 토글한 리스트를 반환한다.
    for i in range(N):
        if A[i] != B[i]:
            A = toggled(A, i)
            answer += 1
            

    print(f"#{test_case} {answer}")