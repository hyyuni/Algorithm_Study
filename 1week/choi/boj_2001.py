T = int(input())

for tc in range(1, T+1):            ## testcase인데 이제 여기는 다 아셔서 설명안할게요
    N, M = map(int, input().split()) 
    a=[]                            ## 빈리스트 만들기 
    result = 0                      ## 최댓값을 뽑아내야 하기 때문에 미리 비교할 결과값 만들어놓기
    for i in range(N):                             
        a.append(list(map(int, input().split())))       ## 입력 받은거 그대로 리스트에 넣기
    for i in range(N-M+1):                              ## 사실 여기서 엄청 헷갈렸었음,,근데 오늘 태은님이 알려주신거 생각하면서 풀었더니 됐어요 감사합니다
        for j in range(N-M+1):
            total = 0
            for k in range(i, i+M):                     ## M*M 칸을 만들어서 합쳐야하니 변수값을 계속 바꾸면서 움직여주기
                for l in range(j, j+M):                 ## 위와 동일
                    total += a[k][l]                    ## 위에 만들었던 total에 더해서 ex) (0,0) -> (0,1) -> (1,0) -> (1,1) / J값 올려서 (0,1)->(0,2) J끝나면 i가 올라가서 아랫줄로 가기
            if result < total:                          ## 최댓값 구하기
                result = total
            else:
                pass
    print(f'#{tc} {result}')                            ##출력하기
            
                
