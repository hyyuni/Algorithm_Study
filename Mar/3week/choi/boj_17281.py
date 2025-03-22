# 내가 이해한것 : 4번타자부터 시작해야함.
# 가장 많은 득점을 하는 타순을 찾아야함? 이게 뭔소리임?
# 0번 인덱스는 무조건 4번째에 칠거임 
# 1이닝에 아웃안되면 다시 반복
# 

# 입력
# N = 이닝수
# N의 줄만큼 각 선수가 이닝에서 얻는 결과


# 주자 진루랑 홈런 아웃 이건 그냥 시뮬레이션 돌리면될거같음
# 문제는 어떻게 순열을 짤것인지기ㅏ 문제인듯,,,
# 이거 순열을 구하는데 9번타자까진데 처음치는건 4번타자가 고정이니
# 8개만 구해서 3번인덱스 즉 4번타자 자리에만 0번 인덱스를 집어 넣으면 될것 같음
# insert이용해서 3번 인덱스에 0 집어넣기 근데 이거 시간초과 안나려나..?
# 점수를 기록한걸 다시 써먹고싶은데,, 일단 풀어보자




# 안타 : 1
# 2루타 : 2
# 3루타 : 3
# 홈런 : 4
# 아웃 : 0

# 아웃 3번이면 이닝 끝
# 아웃 안되면 이닝 계속 진행할거임
# 이닝을 for문을 이용해서 진행하고
# while 문 써서 our < 3: 까지만 진행
# 어떰 

# ㅋㅋ 문제;; python3로 냈다가 시간초과나서 다른사람은 몇초걸렸나 보러 갔는데
# python3로 푼사람 단 한명도없음 시간초과나는듯 python3로 풀면
# pypy3로 풀도록 하세요 여러분들
from itertools import permutations
from pprint import pprint

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for orders in (permutations(range(1, 9), 8)):
    orders = list(orders)
    orders.insert(3, 0) # 3번 인덱스에 0 넣는거임 반대로했다가 디버깅만 20분동안 함 이거하나떄매)
    # 이자리에 ans넣었다가 20분동안 개고생함 이런 사소한 실수좀 줄이자 제발 
    score = 0 # 홈이라고 생각하자
    cur = 0
    for i in range(N):
        out = 0     # 이닝 끝나면 싹다 초기화 시켜줘야 하지않나..? 이문제 떄매 야구 룰 알게되는거같음
        b1 = 0
        b2 = 0
        b3 = 0
        while out < 3: # 어 근데 for 문 돌게되면 while문 끝나면 다시 0부터 시작할텐데..? 그냥 while문 돌면서 cur += 1할까
            if arr[i][orders[cur]] == 0:        # 0부터 시작하는게 아니라 4에서 끝났으면 다음이닝은 5부터 시작해야함 그러자 
                out += 1
            elif arr[i][orders[cur]] == 1:
                score += b3  # 이거 순서 안지키면 안될거같음 먼저 밀어내야함 
                b3 = b2
                b2 = b1
                b1 = 1
            elif arr[i][orders[cur]] == 2:
                score += (b2 + b3)
                b3 = b1
                b1 = 0
                b2 = 1
            elif arr[i][orders[cur]] == 3:
                score += (b1 + b2 + b3)
                b3 = 1
                b2 = 0
                b1 = 0
            elif arr[i][orders[cur]] == 4:
                score += (b1 + b2 + b3 + 1)
                b1 = 0
                b2 = 0
                b3 = 0
            cur = (cur + 1) % 9  # 강사님이 알려준 수법
    ans = max(ans, score)
print(ans)




    #     while out < 3:
    #         for cur in range(9): # 어 근데 for 문 돌게되면 while문 끝나면 다시 0부터 시작할텐데..? 그냥 while문 돌면서 cur += 1할까
    #             if arr[i][orders[cur]] == 0:        # 0부터 시작하는게 아니라 4에서 끝났으면 다음이닝은 5부터 시작해야함 그러자 
    #                 out += 1
    #             elif arr[i][orders[cur]] == 1:
    #                 score += b3  # 이거 순서 안지키면 안될거같음 먼저 밀어내야함 
    #                 b3 = b2
    #                 b2 = b1
    #                 b1 = 1
    #             elif arr[i][orders[cur]] == 2:
    #                 score += (b2 + b3)
    #                 b3 = b1
    #                 b1 = 0
    #                 b2 = 1
    #             elif arr[i][orders[cur]] == 3:
    #                 score += (b1 + b2 + b3)
    #                 b3 = 1
    #                 b2 = 0
    #                 b1 = 0
    #             elif arr[i][orders[cur]] == 4:
    #                 score += (b1 + b2 + b3 + 1)
    #                 b1 = 0
    #                 b2 = 0
    #                 b3 = 0
    #             if out == 3:
    #                 break
    # ans = 
    