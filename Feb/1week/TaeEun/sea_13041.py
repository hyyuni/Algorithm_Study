T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())   # N명의 게으른 사람들 K개의 중요한 일
    a_list = list(map(int, input().split())) # i번째 사람이 고른 일 a 리스트
    b_list = list(map(int, input().split())) # i번째 사람이 설득당하는 시간 b 리스트
    a_set = set(a_list)    #set으로 중복을 없애서 K개 중에 선택당한 일의 숫자를 확인
    a0 = 1
    b_persuasion_target = []
    if len(a_set) == K: 
        ans =0
        # 모두가 K개에 배정된 경우는 따로 계산 필요없이 0으로 초기조건처럼 선언
    else:
        a_b_list = sorted(list(zip(a_list, b_list)),  key=lambda x: (x[0], x[1]))
        # a,b 쌍을 제작하는데 a순서로 정렬하면서 같은 a에서는 b로 정렬(sorted의 key 인자로 조건을 줌)
        for a, b in a_b_list:
            if a0 != a and b_persuasion_target:
                b_persuasion_target.pop()
                # 이전 값과 현재 값이 같지 않으면 전의 값을 다시 빼낸다. 
                # 예를 들어 (1,2) (1,3) (2,1) 같은 경우에 2,1로 넘어간 순간 앞에서 넣은 3을 없앤다.
                # 조건에 and가 붙은 건 빈 리스트일때 pop 오류가 날 수 있으니까
            b_persuasion_target.append(b)
            #b 값만 모아서 왕이 필요로 하는 설득 시간의 합을 구하려고 하는 중
            a0 = a 
            #이전 a값 선언
        if b_persuasion_target:# 리스트가 비었을 경우 제외
        	b_persuasion_target.pop() 
        b_persuasion_target.sort() # 최소 시간의 합이라 정렬후 앞에거만 자를 예정
        persuasion_number = max(0, K-len(a_set)) #오류가 나길래 혹시나 음수의 가능성 때문인가 싶어서 추가
        ans = sum(b_persuasion_target[:persuasion_number]) #최소 시간의 합이 답!
    print(f'#{tc} {ans}')
