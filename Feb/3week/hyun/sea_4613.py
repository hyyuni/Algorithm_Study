T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    max_v = 0
    cnt = 0
    ans = 0

    # W, B, R에서 R이 무조건 한줄 차지해야 하므로 B는 즉, sj = N-1까지 칠해질 수 있다
    for si in range(0, N-2):
        for sj in range(si+1, N-1):
            cnt = 0
            for i in range(si+1): # 'W' 얼만큼?
                cnt += arr[i].count('W')
            for j in range(si+1, sj+1): # 'B' 얼만큼?
                cnt += arr[j].count('B')
            for k in range(sj+1, N): # 'R' 얼만큼?
                cnt += arr[k].count('R')
            max_v = max(max_v, cnt)
    # W, B, R이 제일 많이 칠해져 있는 상태일 때 전체에서 max를 빼주면 칠할 최솟값이 나옴
    ans = N * M - max_v
    print(f'#{tc} {ans}')