def sdoku_solve(sdoku):
    #행 
    for sdo in sdoku:
        if len(set(sdo)) != 9:
            return 0
    #열
    list_t = list(zip(*sdoku)) #전치행렬 만드는 코드
    for lt in list_t:
        if len(set(lt)) != 9:
            return 0
    #3*3
    for i in range(0,9,3):
        for j in range(0,9,3):
            list_3 = sdoku[i][j:j+3] + sdoku[i+1][j:j+3] + sdoku[i+2][j:j+3]
        if len(set(list_3)) != 9:
            return 0
    return 1

 


T = int(input())

for test_case in range(1,T+1):
    sdoku = [list(map(int,input().split())) for _ in range(9)]
    print(f'#{test_case} {sdoku_solve(sdoku)}')
