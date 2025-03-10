# 보물상자 비밀번호
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo&

# 1. 만들 수 있는 수를 만든다. *중복 주의. *N번마다 반복한다.
#    어차피 회전별로 비밀번호를 저장하는게 아니기 때문에 그냥 계속 반복하면서 구하면 되다. (회전 하면서 만들어진 전체 비밀번호 목록에서 K번째 구하는 것이므로)
# 2. 내림차순으로 정렬한다.
# 3. K번째로 큰 수를 10진수로 만든다.
#    16진수를 10진수로 만들기. 

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("swea_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # 숫자의 개수, 크기 순서 K
    answer = 0
    pw = input().strip()
    candidates = set()

    for i in range(N // 4):
        pw = pw[1:] + pw[0]  
    
        for j in range(0, N, (N // 4)):
            candidates.add((pw[j : j+(N // 4)]))

    candidates = list(candidates)
    candidates.sort(reverse=True)
    answer = int("0x" + candidates[K-1], 16)
    
    print(f"#{test_case} {answer}")