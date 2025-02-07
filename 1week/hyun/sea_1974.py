T = int(input())
for tc in range(1, T+1):
    # 스도쿠 퍼즐을 리스트 컴프리헨션으로 생성
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 0
    # 스도쿠 퍼즐을 검사하기 위한 함수 생성
    def checklist(arr):
        sort_list = list(range(1,10))
        check_list= arr[:]
        if check_list == sort_list:
            return check_list is True

    # 가로 검사
    for i in range(9):
        checklist(arr[i])
        if True:
            ans +=1
    
    # 세로 검사
    for j in range(0, 9):
        for i in range(0, 9):
            checklist(arr[i][j])
            if True:
                ans +=1

    if ans == 18:
        print(1)
    else:
        print(0)

    print(f'{tc} {ans}') 
