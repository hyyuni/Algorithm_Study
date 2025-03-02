# magnetic

import sys
sys.stdin = open("input (8).txt", "r")

T = 100
for tc in range(1, T+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    ans = 0 

    # N극
    for j in range(n):
        stack = []
        for i in range(n):
            if graph[i][j] == 1:
                stack.append(1) # N극 저장
            elif graph[i][j] == 2:
                stack.append(2) # S극 저장

        idx = 0 # N극 S극 이동 하기기
        for k in range(len(stack)):
            graph[idx][j] = stack[k]
            idx += 1
        
        while idx < n: # 나머지는 0
            graph[idx][j] = 0
            idx += 1
    # 교착 상태 카운팅
    for j in range(n):
        found_n = False # flag 변수 설정
        for i in range(n):
            if graph[i][j] == 1:
                found_n = True
            elif graph[i][j] == 2 and found_n:
                ans += 1
                found_n = False # 다음 교착 찾기 위해 초기화
    
    print(f'#{tc} {ans}')