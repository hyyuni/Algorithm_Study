# 백만 장자 프로젝트 
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    max_price = 0
    tot = 0 

    for i in range(N-1, -1, -1): # 뒤에서부터 높은 가격 찾기
        if price[i]>max_price:
            max_price = price[i]
        else:
            tot += (max_price-price[i]) # 낮은 가격 만나면 높은 가격에서 빼주어 총 이익 구하기

    print(f'#{tc} {tot}')