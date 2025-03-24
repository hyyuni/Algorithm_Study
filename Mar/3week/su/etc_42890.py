# https://school.programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations

def solution(relation):
    answer = []
    all_combi = []
    r_col = len(relation[0])
    r_row = len(relation)
    
    def recur(start_i, temp):
        if temp != []:
            all_combi.append(temp[:])
        for i in range(start_i, r_col):
            temp.append(i)
            recur(i+1, temp)
            temp.pop()
    
    recur(0, []) # 모든 조합 구하기
    all_combi.sort(key=lambda x: (len(x), x))
    for combi in all_combi:
        key_li = []
        for rel in relation:
            key_temp = []
            for key in combi:
                key_temp.append(rel[key])
            key_li.append(tuple(key_temp))
        
        if len(set(key_li)) != len(key_li):
            continue
        # 최소성
        flag = False
        for i in range(len(answer)):
            if flag:
                break
            if set(answer[i]).issubset(set(combi)):
                flag = True
                break
        if not flag:
            answer.append(combi)
    return len(answer)