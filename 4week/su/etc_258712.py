# https://school.programmers.co.kr/learn/courses/30/lessons/258712
# 가장 많이 받은 선물
from collections import defaultdict
def solution(friends, gifts):
    answer = 0
    n = len(friends)
    answer_li = [0] * n
    info = [[0] * n for _ in range(n)]
    index_dict = defaultdict(int)
    score = [0] * n
    for i in range(n):
        index_dict[friends[i]] = i
        
    for gift in gifts:
        giver, taker = gift.split(" ")
        giver_i, taker_i = index_dict[giver], index_dict[taker]
        info[giver_i][taker_i] += 1
        
    # info 확인하면서 선물지수 계산하기
    for i in range(n):
        give_pr = 0
        taken_pr = 0
        for j in range(n):
            if i == j:
                continue
            give_pr += info[i][j]
            taken_pr += info[j][i]
        score[i] = give_pr - taken_pr # 선물지수 입력
    
    # 선물 확인
    for i in range(n):
        # print(i, "i")
        for j in range(i+1, n):
            # print(j)
            # 선물기록이 없거나(둘다 0이거나), 둘다 같은 경우
            if info[i][j] == info[j][i]:
                 # 선물 기록이 없거나 같은 경우
                if score[i] > score[j]:
                    answer_li[i] += 1
                elif score[i] < score[j]:
                    answer_li[j] += 1
                continue
            # if info[i][j] or info[j][i]: # 주고받은 기록이 있는 경우, 많이 준 사람이 받는다.
            if info[i][j] > info[j][i]:
                answer_li[i] += 1
            elif info[i][j] < info[j][i]:
                answer_li[j] += 1
                
    return max(answer_li)