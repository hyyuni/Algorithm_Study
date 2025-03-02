# 어디에 단어가 들어갈 수 있을까
T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    # 연속된 1의 길이가 k보다 커야함

    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[i][j] == 1: # 1 만나면 카운트 증가
                cnt += 1
            if puzzle[i][j] == 0 or j == n-1: # 0 만났을 때, 인덱스 처리
                if cnt == k: # 카운트가 k면 ans 증가
                    ans += 1
                cnt = 0   # 0을 만났을 때 카운트 개수가 1이 아니면 카운트 초기화

        for j in range(n):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == n-1:
                if cnt == k:
                    ans += 1
                cnt = 0

    print(f'#{tc} {ans}')