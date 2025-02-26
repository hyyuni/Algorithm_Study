'''
# 필요 데이터

- 전역: 10개로 정해짐
- TC당 필요 데이터 : magnetic(arr), cnt

# 로직(TC에 들어왔다고 가정)
1. 입력
  magnetic의 배열

2. 열을 행으로 전치행렬처리 (list로 편하게 보기)

3. 행 단위로 검사하며 교착 상태가 가능한 자석 찾기
      for m in lst:
        pre_m = 0 (리스트 마다 pre_m 값은 초기화가 필요함)
  	    if m == 2 and pre_m == 1:
	        cnt +=1
	        pre_m = 0 # 교착 후 갱신

'''
for tc in range(1, 11):
    N = int(input())
    # 1. magnetic 배열 받기
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # 2. 전치행렬 만들기
    arr2 = list(zip(*arr))
    # 3. 행 단위로 검사하며 교착 상태가 가능한 자석 찾기
    for lst in arr2:
        pre_m = 0
        for m in lst:
            if m ==1:
                pre_m = 1 # N극이 발견됐을 때 체크 시작
            elif m == 2 and pre_m ==1:
                cnt += 1
                pre_m = 0 # 이전 자석 갱신

    print(f'#{tc} {cnt}')