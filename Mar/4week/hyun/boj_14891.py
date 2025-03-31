import sys
sys.stdin = open('input.txt', 'r')

'''
clockwise = 1, counter_clockwise = -1, N극 = 0, S극 = 1

arr는 12시 방향부터(기준) 시계방향
다른 극성일 때, 회전은 2가지 경우가 있음
1. (1) 반시계 방향 움직임 -> (2) 옆에는 시계 방향 움직임
2. (1) 시계 방향 움직임 -> (2) 옆에는 반시계 방향 움직임
2개의 명령 수행 후 같은 극성으로 정렬 되면 break
'''

N = 4
dir_12 = [0]*(N+1) # 12시 방향 리스트(시계방향 idx -1, 반시계방향 idx +1)
arr = [[0]*8] + [list(map(int,input())) for _ in range(N)] # idx 번호 맞추기 위해 패딩
K = int(input())


for _ in range(K):
    idx, dir = map(int, input().split())
    temp = [(idx, 0)]

    # 톱니를 회전하며 우측 방향에서 같은 극성이 나온다면 break
    for i in range(idx+1, N+1):
        if arr[i-1][(dir_12[i-1]+2)%8] != arr[i][(dir_12[i]+6)%8]:
            temp.append((i, (i-idx)%2))
        else:
            break
    # 톱니를 회전하며 좌측 방향에서 같은 극성이 나온다면 break        
    for i in range(idx-1, 0, -1):
        if arr[i][(dir_12[i]+2)%8] != arr[i+1][(dir_12[i+1]+6)%8]:
            temp.append((i, (idx-i)%2))
        else:
            break
    
    # 회전 처리
    for idx, rotate in temp:
        if rotate==0:
            dir_12[idx] = (dir_12[idx]-dir+8)%8
        else:
            dir_12[idx] = (dir_12[idx]+dir+8)%8
    
ans = 0
# 회전한 점수 계산하기
score = [0, 1, 2, 4, 8]
for i in range(1, N+1):
    ans += arr[i][dir_12[i]]*score[i]

print(ans)