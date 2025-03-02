import sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("boj_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().strip().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
# visited = [[[-1, -1]] * M for _ in range(N)] # 얕은 복사 오류
visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]
# print(visited)
queue = deque()
queue.append((0, 0, 0)) # row, col, 벽 부쉈는지
visited[0][0][0] = 1
visited[0][0][1] = 1

INF = int(1e9)
answer = INF

while queue:
    row, col, crushed = queue.popleft()
    if (row, col) == (N-1, M-1):
        answer = min(visited[row][col][crushed], answer)
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            continue
        if visited[nr][nc][crushed] != -1:
            continue

        if graph[nr][nc] == 1: # 벽인 경우
            if crushed == 1: 
                continue # 이미 벽 부쉈던 경우 다시 벽을 부실 수 없다.
            # 벽 아직 안 부신 경우
            visited[nr][nc][1] = visited[row][col][crushed] + 1 # 거리 업데이트
            queue.append((nr, nc, 1))
        else: # 벽이 아닌 경우
            visited[nr][nc][crushed] = visited[row][col][crushed] + 1
            queue.append((nr, nc, crushed))

print(answer if answer != INF else -1)
