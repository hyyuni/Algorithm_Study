T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = list(map(str, input().split()))
    # 카드를 퍼펙트 셔플 하기 위한 리스트 생성
    lst1 = []
    lst2 = []
    ans = []

    if N % 2 == 0: # 짝수이면 그냥 N//2만큼 순회하면 됨
        for i in range(N//2):
            lst1.append(card[i])
            for j in range(i+N//2, N):
                    lst2.append(card[j])
    else:
        for i in range(N//2+1): # 홀수이면 lst1은 N//2+1만큼 순회해야 함
            lst1.append(card[i])
            for j in range(i+N//2+1, N):
                    lst2.append(card[j])

    for i in range(N//2): # N//2 만큼 반복문을 돌며 ans리스트에 카드 추가
         ans.append(lst1[i])
         ans.append(lst2[i])
    else:
         if N % 2 == 1: # 만약에 홀수라면 더해지지 않은 카드를 마지막에 추가
              ans.append(lst1[-1])
    
    print(f'#{tc} {" ".join(ans)}')
