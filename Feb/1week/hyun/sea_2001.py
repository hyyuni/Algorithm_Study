T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 파리 2차원 배열 리스트 생성
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 파리의 누적합 배열 생성 (index는 0부터 시작이므로 처음 누적값을 위해 N+1까지)
    prefix = [[0] * (N + 1) for _ in range(N + 1)]
    # 정답 값 초기화
    ans = 0

    # 누적 합 만들기
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            prefix[i][j] = (
                arr[i - 1][j - 1]  # 현재 위치 값
                + prefix[i - 1][j]  # 위쪽 값
                + prefix[i][j - 1]  # 왼쪽 값
                - prefix[i - 1][j - 1]  # 중복된 부분 제거
            )    

    # 파리 퇴치하기    
    for fi in range(N - M + 1):  # 파리채 영역이 0부터 N-M까지임
        for fj in range(N - M + 1):
            sum_fly = (
                prefix[fi + M][fj + M]   # 전체 영역
                - prefix[fi][fj + M]     # 위쪽 잘라내기
                - prefix[fi + M][fj]     # 왼쪽 잘라내기
                + prefix[fi][fj]         # 겹친 부분 다시 더하기
            )
            ans = max(ans, sum_fly)  # 최댓값 갱신
    
    print(f'#{tc} {ans}')