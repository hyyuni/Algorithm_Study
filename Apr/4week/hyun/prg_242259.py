from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def solution(land):
    N, M = len(land), len(land[0])
    visited = set()
    oils = [0]* M

    def bfs(sy,sx):
        q = deque([(sy,sx)])
        visited.add((sy,sx))
        cnt = 1
        columns = {sx}

        while q:
            cy, cx = q.popleft()

            for dir in range(4):
                ny = cy + dy[dir]
                nx = cx + dx[dir]

                if not (0<=ny<N and 0<=nx<M):
                    continue

                if land[ny][nx] == 1 and (ny,nx) not in visited:
                    visited.add((ny,nx))
                    q.append((ny,nx))
                    cnt += 1
                    columns.add((nx))

        for column in columns:
            oils[column] += cnt

    
    for y in range(N):
        for x in range(M):
            if land[y][x] and (y,x) not in visited:
                bfs(y, x)

    return max(oils)