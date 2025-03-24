
import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("swea_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

from collections import deque

# 입력 받기
gears = [deque(map(int, input().strip())) for _ in range(4)]
K = int(input())

# 기어 회전 함수
def spin(gear, direction):
    if direction == -1:  # 반시계 방향
        gears[gear].append(gears[gear].popleft())
    else:  # 시계 방향
        gears[gear].appendleft(gears[gear].pop())

# 회전할 기어들 결정
def check_rotation(start, direction):
    rotate_state = [0] * 4  # 각 기어의 회전 방향 (0: 회전 X, 1: 시계, -1: 반시계)
    rotate_state[start] = direction  # 시작 기어의 회전 방향 설정

    # 왼쪽으로 전파 (start 기어의 왼쪽 기어들 확인)
    for i in range(start, 0, -1):
        if gears[i][6] != gears[i-1][2]:  # 맞닿은 극이 다르면 회전
            rotate_state[i-1] = -rotate_state[i]
        else:
            break

    # 오른쪽으로 전파 (start 기어의 오른쪽 기어들 확인)
    for i in range(start, 3):
        if gears[i][2] != gears[i+1][6]:  # 맞닿은 극이 다르면 회전
            rotate_state[i+1] = -rotate_state[i]
        else:
            break

    return rotate_state

# K번 회전 수행
for _ in range(K):
    gear, direction = map(int, input().strip().split())
    gear -= 1  # 0-indexed 변환

    # 회전 여부 결정
    rotate_state = check_rotation(gear, direction)

    # 실제 회전 수행
    for i in range(4):
        if rotate_state[i] != 0:
            spin(i, rotate_state[i])

# 점수 계산
score = sum((gears[i][0] * (2 ** i)) for i in range(4))
print(score)
