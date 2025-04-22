T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def delta(sy, sx):
    res = graph[sy][sx]

    for dir in range(4):
        for d in range(1,N):
            ny = sy + dy[dir] * d
            nx = sx + dx[dir] * d

            if not (0<=ny<N and 0<=nx<N):
                break

            res += graph[ny][nx]
    
    return res


for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    min_v = float('inf')
    for y in range(N):
        for x in range(N):
            max_v = max(max_v, delta(y, x))
            min_v = min(min_v, delta(y, x))
    
    ans = max_v - min_v

    print(f'#{tc} {ans}')