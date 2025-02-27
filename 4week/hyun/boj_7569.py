from collections import deque

def bfs():
    q = deque()

    cnt = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 1: # 3차원을 순회하면서 익은 토마토를 찾았다면,
                    q.append((h,n,m)) # 현재 좌표 튜플로 넣어주기
                    visited[h][n][m] = 1
                elif tomato[h][n][m] == 0: # 안 익은 토마토라면
                    cnt += 1
    
    while q:
        ch, cn, cm = q.popleft()
        # 2차원 상,하,좌,우 + 3차원 위 아래 델타 탐색
        for dh, dn, dm in ((0,-1,0), (0,1,0), (0,0,-1), (0,0,1), (-1,0,0), (1,0,0)):
            nh, nn, nm = ch+dh, cn+ dn, cm + dm
            if nh < 0 or nh >= H or nn < 0 or nn >= N or nm < 0 or nm >= M:
                continue
            if visited[nh][nn][nm] == 0 and tomato[nh][nn][nm] == 0:
                q.append((nh,nn,nm))
                visited[nh][nn][nm] = visited[ch][cn][cm] + 1
                cnt -= 1
    if cnt == 0:
        return visited[ch][cn][cm] -1 # 처음에 방문처리 1로 하고 시작했으므로 답은 1개를 빼줘야 함
    else:
        return -1

M, N, H = map(int, input().split())
# 토마토, 3차원 배열 생성하기
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# 3차원 방문 리스트 생성
visited = [[[0] *M for _ in range(N)] for _ in range(H)]

res = bfs()
print(res)