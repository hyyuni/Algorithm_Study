# 퍼펙트 셔플
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(str, input().split()))
    left = [] # 먼저 놓을 카드
    right = []
    result = []
    if N % 2 == 0:
        for i in range(N):
            if i >= N//2:
                right.append(cards[i])
            else:
                left.append(cards[i])
    else:
        for i in range(N):
            if i > N//2:
                right.append(cards[i])
            else:
                left.append(cards[i])
    for i in range(N//2):
        result.append(left[i])
        result.append(right[i])
    if N % 2 == 1: # 홀수일 경우
        result.append(left[N//2]) # left의 가장 마지막 요소 추가

    print(f'#{tc}', end =' ')
    for card in result:
        print(card, end = ' ')
    print()