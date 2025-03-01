from collections import deque

for tc in range(1, 11):
    T = int(input())
    q = deque(list(map(int, input().split())))

    cnt = 1 # 감소하는 숫자 카운팅

    while True:
        cur_pos = q.popleft()
        cur_pos -= cnt # 현재 뽑아낸 암호를 cnt 만큼 감소시키기
        cnt += 1

        if cnt > 5: # 카운팅이 5를 넘어간다면 초기화
            cnt = 1
        if cur_pos <= 0: # 마지막에 뽑아낸 숫자가 0 이하가 된다면 0을 추가하고 반복문 종료
            q.append(0) # 큐 마지막에 0을 추가
            break
        
        q.append(cur_pos) # 해당 조건에 걸리지 않으면 감소시킨 숫자를 큐에 추가
    
    print(f'{tc}', *q)