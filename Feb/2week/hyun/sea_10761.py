T = int(input())

for tc in range(1, T+1):
    test = input().split()
    N = int(test[0])
    button = test[1:]
    time = 0
    
    robot = {'O': 1, 'B': 1}
    robot_time = {'O': 0, 'B': 0}
    temp = [] # (로봇, 버튼번호) 저장할 빈 리스트

    for i in range(N): # temp에 (로봇, 버튼번호) 튜플로 저장하기
        temp.append((button[i*2], int(button[i*2 +1])))

    for i in range(N): # 튜플을 언패킹하기
        robot_color, robot_button = temp[i]

        # 현재 로봇이 버튼을 누르기까지 걸리는 시간 
        move_time = abs(robot_button - robot[robot_color])

        # 버튼 누르는 시간 갱신하기
        robot_time[robot_color] = max(robot_time[robot_color] + move_time, time) +1
        time = robot_time[robot_color]

        # 로봇이 움직인 위치 변경
        robot[robot_color] = robot_button

    print(f'#{tc} {time}')

    