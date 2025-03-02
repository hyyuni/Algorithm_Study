T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    bl_cnt, wh_cnt = 0, 0

    # 1. 그래프 정 가운데에 백, 흑 놓고 시작하기
    m = N // 2
    graph[m][m] = graph[m + 1][m + 1] = 2
    graph[m][m + 1] = graph[m + 1][m] = 1

    # 2. 돌 놓기 및 뒤집기
    for _ in range(M):
        sx, sy, d = map(int, input().split())
        graph[sx][sy] = d

        # 8방향 탐색
        for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)):
            r = []
            for multi in range(1, N):
                nx, ny = sx + dx * multi, sy + dy * multi
                if nx < 1 or nx > N or ny < 1 or ny > N or graph[nx][ny] == 0:
                    break
                if graph[nx][ny] == d:
                    while r:
                        tx, ty = r.pop()
                        graph[tx][ty] = d
                    break
                r.append((nx, ny))

    # 3. 돌 개수 세기
    for lst in graph[1:]:
        bl_cnt += sum(1 for x in lst[1:] if x == 1)
        wh_cnt += sum(1 for x in lst[1:] if x == 2)

    print(f'#{tc} {bl_cnt} {wh_cnt}')