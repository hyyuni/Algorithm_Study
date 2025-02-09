N = int(input())                        ## 원래는 카운팅정렬을 사용하려했었습니다.
N_num = list(map(int, input().split())) ## 근데 천만개의 리스트를 만들어서 하기엔 시간초과가 날 것 이라고 생각해 
M = int(input())                        ## 어떻게 할까 하다가 10이란 걸 저장해두고 거기에 하나씩 더하는 방식은 어떨까 해서 생각해본결과
M_num = list(map(int, input().split())) ## 딕셔너리를 이용하기로 했습니다.
dic = {}
for i in N_num:                         ## 근데 내일인 2월 10일 월요일에 이진탐색을 배우더라구요!
    if i in dic:                        ## 내일 이진탐색을 배워서 반 나눠서 하는 방식으로 풀어보고싶다는 생각이 들었습니다.
        dic[i] += 1
    else:
        dic[i] = 1

for j in M_num:
    if j in dic:
        print(dic[j], end=" ")
    else:
        print(0, end=" ")