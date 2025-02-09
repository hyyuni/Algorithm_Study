# M*M크기 최대합 구하기

import sys
sys.stdin = open("swea_input.txt", "r")
input = sys.stdin.readline

from collections import deque
from collections import defaultdict

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    # 맨 왼쪽 상단 모서리를 기준으로 M*M크기를 탐색한다.
    max_cell = 0
    for cur_r in range(N):
        for cur_c in range(N):
            queue = deque()
            queue.append((cur_r, cur_c))

            visited = defaultdict(bool) # 인덱스 처리가 복잡할 것 같아 이중 리스트 대신 딕셔너리 형태로 방문처리한다.
            
            cell = arr[cur_r][cur_c]
            visited[(cur_r, cur_c)] = True

            cnt = 0
            # 4방향(상하좌우) 탐색..은 안된다.
            # 상측, 좌측까지 탐색하면 M*M 크기보다 탐색 영역이 넓어지기 때문이다.
            # 시작 위치를 기준으로 오른쪽&하단으로 점차 퍼지면서 탐색해야 한다.
            # dr = [-1, 0, 1, 0] 
            # dc = [0, 1, 0, -1]

            # 2방향(우,하) 탐색
            dr = [0, 1]
            dc = [1, 0]
            while queue:
                r, c = queue.popleft()
                for i in range(2):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr < 0 or nc < 0 or nr >= N or nc >= N:
                        continue
                    if nr >= cur_r + M or nc >= cur_c + M:
                        continue
                    if (nr, nc) in visited:
                        continue
                    cnt += 1

                    visited[(nr, nc)] = True
                    cell += arr[nr][nc]
                    queue.append((nr, nc))

            if cell > max_cell:
                max_cell = cell
    print(f"#{t} {max_cell}")