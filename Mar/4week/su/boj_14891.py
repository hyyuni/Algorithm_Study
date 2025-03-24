import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("boj_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

import pprint
import copy

gears = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())
INF = int(1e9)

def spin(gear, direction):
    global copied
    if direction == -1:  # 이 기어가 반시계 방향으로 돌 때
        copied[gear] = gears[gear][1:] + [gears[gear][0]]
    else:
        copied[gear] = [gears[gear][-1]] + gears[gear][:-1]

    

def connected(pre_idx, pos, direction):  
    global copied, gears
    if pos == 0:
        spin(pre_idx, direction)
        return
    
    next_direction = direction
    next_idx = pre_idx + pos
    while True:
        # 인덱스 벗어나는 경우
        if next_idx >= 4 or next_idx < 0:  
            break

        # 원래 톱니바퀴와 옆에 있는 톱니바퀴 부품이 같은 극인 경우
        if pos == 1:  # 오른쪽 기어가 돌아가려는 경우
            cur_piece, next_piece = (2, 6)
        elif pos == -1:  # 왼쪽 기어가 돌아가려는 경우
            cur_piece, next_piece = (6, 2)
        if gears[pre_idx][cur_piece] == gears[next_idx][next_piece]:  
            break

        next_direction = next_direction * -1
        spin(next_idx, next_direction)
        pre_idx = next_idx
        next_idx += pos

# pos: -1, 0, 1 -> 왼쪽, 가운데, 오른쪽
for _ in range(K):
    gear, direction = map(int, input().strip().split())
    gear -= 1
    copied = copy.deepcopy(gears)
    connected(gear, 0, direction)
    connected(gear, -1, direction)
    connected(gear, 1, direction)
    # gears[:] = copied
    # gears = copy.deepcopy(copied)
    gears = copied
    # pprint.pprint(gears)

# pprint.pprint(gears)
answer = 0
score = [1, 2, 4, 8]
for i in range(4):
    if gears[i][0] == 1:
        answer += score[i]

print(answer)
