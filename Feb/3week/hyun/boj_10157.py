C, R = map(int, input().split())
K = int(input())

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
dir = 0

# 범위 계산을 생략하기 위해 arr 주변을 1값으로 패딩하기
arr = [[1]*(C+2)] + [[1]+[0]* C+[1] for _ in range(R)] +[[1]*(C+2)]

if C * R < K: # 좌석 배정이 불가능한 경우
    print(0)
else: # K가 될 때, 좌표 출력하기

    ci, cj = 1, 1 # 패딩했으므로, 인덱싱은 (0,0)이 아닌 (1,1)부터 시작
    for n in range(1, K):
        arr[ci][cj] = n
        ni = ci + di[dir]
        nj = cj + dj[dir]
        if arr[ni][nj] == 0: # 좌표가 비어있으니 이동 가능
            ci, cj = ni, nj
        else:
            dir = (dir+1) % 4 # 방향 전환
            ci = ci+di[dir]
            cj = cj+dj[dir]
    print(f'{cj} {ci}')