T = int(input())

def checkList(arr):
    global cnt
    i = 0
    while i <= N - K:
        if sum(arr[i:i+K]) == K: # K개의 1이 연속되는 경우
            if (i==0 or arr[i-1] ==0) and (i+K == N or arr[i+K] == 0):
                #앞 뒤에 1이 더이상 없는 지 확인
                cnt += 1
            i += K # K만큼 건너뛰기
        else:
            i += 1 # 1만큼 건너뛰기
            
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # 가로 검사
    for i in range(N):
        checkList(puzzle[i])

    # 세로검사
    for i in range(N):
        column = [puzzle[j][i] for j in range(N)]
        checkList(column)

    print(f'#{tc} {cnt}')