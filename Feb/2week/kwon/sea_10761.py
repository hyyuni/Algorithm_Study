# 신뢰
# 매 1초마다 로봇은 양방향으로 1만큼 걷거나, 자기 위치에 있는 버튼을 누르거나 아무 것도 하지 않음
# 동시에 버튼을 누를 수 없음

T = int(input())
for tc in range(1, T+1):
    button = list(map(str, input().split())) # 버튼의 개수, 버튼
    N = int(button[0]) # 버트 개수
    time = 0 # 이동, 버튼 누를 때마다 +1초
    b = [1] # 블루 버튼, 1에서 출발
    o = [1] # 오렌지 버튼
    move_b = 0 # 이동 시간
    move_o = 0
    push_b = 0 # 버튼 누르는 시간 계산
    push_o = 0
    result = 0

    for i in range(1, 101): # 버튼 100개
        if i % 2 == 1 and i +1 <len(button):
            if button[i] == 'B':
                b.append(int(button[i+1]))
            else:
                o.append(int(button[i+1]))
    push_o = len(o) - 1
    push_b += len(b) - 1

    for i in range(1, len(b)):
        move_b += b[i] - b[i-1] #이동 시간 계산 : 리스트 값 차이 이용
    for i in range(1, len(o)):
        move_o += o[i] - o[i-1]

    move = move_b if move_b > move_o else move_o # 이동시간 중복 처리

    result = move + push_b + push_o
    print(f'#{tc} {result}')

# 시간 부족....ㅎㅎ