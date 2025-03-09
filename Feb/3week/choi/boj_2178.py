from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]



def BFS(x,y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            di, dj = x + dx[i], y + dy[i]
            if 0 <= di < N and 0 <= dj < M and arr[di][dj] == 1:
                arr[di][dj] = arr[x][y] + 1
                queue.append((di, dj))
    return arr[N-1][M-1]
    
    
print(BFS(0,0))