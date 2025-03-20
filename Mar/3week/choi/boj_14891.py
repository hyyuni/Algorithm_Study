from collections import deque

def wheel_rotate(start, dir):
    to_rotate = [(start, dir)]
    
    # 왼쪽
    cur_dir = dir
    for i in range(start, 0, -1):
        if wheel[i][6] != wheel[i - 1][2]:
            cur_dir = -cur_dir
            to_rotate.append((i - 1, cur_dir))
        else:
            break
    
    # 오른쪽
    cur_dir = dir
    for i in range(start, 3):
        if wheel[i][2] != wheel[i + 1][6]:
            cur_dir = -cur_dir
            to_rotate.append((i + 1, cur_dir))
        else:
            break
    
    # 회전 적용
    for i, d in to_rotate:
        wheel[i].rotate(d)

wheel = [deque(map(int, input())) for _ in range(4)]
k = int(input())

for _ in range(k):
    idx, d = map(int, input().split())
    wheel_rotate(idx - 1, d)

score = 0  

for i in range(4):  
    if wheel[i][0] == 1: 
        score += 2 ** i 

print(score)
