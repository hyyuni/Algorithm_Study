# 홈 방법 서비스

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N : 도시의 크기 M : 집이 지불할 수 있는 비용
    city = [list(map(int, input().split())) for _ in range(N)]
    house_list = []

    for i in range(N):  # 집 좌표
        for j in range(N):
            if city[i][j] == 1:
                house_list.append((i, j))

    max_ans = 0
    for k in range(1, N + 2):  # k의 최대값 : N+1
        for i in range(N):
            for j in range(N):
                ans = 0
                for r, c in house_list:
                    if abs(i - r) + abs(j - c) < k:
                        ans += 1
                    if ans * M - (k * k + (k - 1) * (k - 1)) >= 0:  # k*k + (k-1)*(k-1)  운영비용
                        # 손해보지 않고 =  이익이 없어도 됨 => profit >= 0
                        max_ans = max(max_ans, ans)
    print(f'#{tc} {max_ans}')
