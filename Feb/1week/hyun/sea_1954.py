T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 달팽이를 만들 초기화 리스트 선언
    temp = [[0]*N for _ in range(N)]

    # 초기값 설정
    i, j = 0, 0
    snail = 1
    temp[i][j] = snail

    # 달팽이의 상하좌우 변경 (오른쪽-> 아래 -> 왼쪽 -> 위 -> 오른쪽으로 순회)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    dir = 0 # si, sj를 인덱싱해 방향을 바꾸기 위한 변수

    # 달팽이 반복문
    while snail < N * N:
        si = i + di[dir]
        sj = j + dj[dir]
        # idx 범위 내에 있거나 값이 0인 경우
        if 0 <= si < N and 0 <= sj < N and temp[si][sj] == 0:
            i, j = si, sj
            snail += 1
            temp[i][j] = snail # 달팽이 칸 채우기 
            
        else: # idx를 넘어가거나 값이 0이 아니라면 방향 체인지
            dir = (dir +1) % 4
                
    
    print(f'#{tc}')
    for ans in temp:
        print(*ans)



            