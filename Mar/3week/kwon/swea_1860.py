# 진기의 최고급 붕어빵
T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  
    customers = list(map(int, input().split())) 
    customers.sort()
    
    max_time = max(customers)  
    bbang = [0] * (max_time + 1)  
    
    # 붕어빵 굽기
    for i in range(M, max_time + 1, M):
        bbang[i] += K  #
    
    result = 'Possible'  
    
    for customer in customers:
        if bbang[customer] > 0:  # 고객이 오는 시간에 붕어빵이 있으면
            bbang[customer] -= 1  # 붕어빵 하나 소모
        else:
            result = 'Impossible' 
            break  
    
    print(f'#{tc} {result}')
