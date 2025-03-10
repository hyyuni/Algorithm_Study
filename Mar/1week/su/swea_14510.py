import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("swea_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

# T = 10
# 수정 필요한 코드입니다.
T = int(input())
def get_idx(remainder):
    temp_idx = -1
    for i in range(N):
        if needed[i] == 0:
            # temp_idx = -2
            continue

        if needed[i] % 2 == remainder:
            temp_idx = i
            break

        elif temp_idx == -1:
            temp_idx = i  # 원하는 인덱스 못찾은 경우에 값이 있는 거라도 리턴하게 설정

    return temp_idx

for test_case in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_h = max(trees)
    needed = [max_h - h for h in trees]
    max_days = sum(needed)  # 하루에 1일씩 준다고 가정한다면 최대일수 ..? sum(needed) // 3 + 2
    answer = 0

    for i in range(1, max_days):
        print(f"--------BEFORE: {i}일째, needed: {needed}----------")
        remain = i % 2
        idx = get_idx(remain)
        if idx == -1:  # 물줘야 되는 게 다 0된 경우. 즉, 다 물을 준 경우
            print(f"#{test_case} {i}")
            break
        needed[idx] -= 2 if remain == 0 else 1  # 홀수날짜면 1빼고 짝수날짜면 2빼기
        print(f"AFTER: {i}일째, needed: {needed}")
