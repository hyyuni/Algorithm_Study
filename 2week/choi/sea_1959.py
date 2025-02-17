T = int(input())

for tc in range(1, T+1):
    result = 0
    NA, MB = map(int, input().split())
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    
    if MB > NA:
        for i in range(MB-NA+1):
            hana = 0
            for j in range(NA):
                hana += A_list[j] * B_list[j+i]
            if hana >= result:
                result = hana
    elif NA > MB:   
        for i in range(NA-MB+1):
            hana = 0
            for j in range(MB):
                hana += A_list[j+i] * B_list[j]
            if hana >= result:
                result = hana
    else:
        hana = 0
        for j in range(MB):
            hana += A_list[j] * B_list[j]
    print(f'#{tc} {result}')