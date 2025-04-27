from collections import deque

# Union-Find용 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 섬에 번호 붙이기
def labeling(board, n, m):
    island_num = 1
    islands = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                islands[i][j] = island_num

                while queue:
                    x, y = queue.popleft()
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if 0 <= nx < n and 0 <= ny < m:
                            if board[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                islands[nx][ny] = island_num
                                queue.append((nx, ny))
                island_num += 1

    return islands, island_num - 1

# 다리 후보 찾기
def find_bridges(islands, n, m):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    edges = []

    for i in range(n):
        for j in range(m):
            if islands[i][j] > 0:
                current_island = islands[i][j]
                for dir in range(4):
                    length = 0
                    nx = i + dx[dir]
                    ny = j + dy[dir]
                    while 0 <= nx < n and 0 <= ny < m:
                        if islands[nx][ny] == current_island:
                            break  # 자기 섬이면 멈춤
                        elif islands[nx][ny] == 0:
                            length += 1
                            nx += dx[dir]
                            ny += dy[dir]
                        else:
                            # 다른 섬 발견
                            if length >= 2:
                                edges.append((length, current_island, islands[nx][ny]))
                            break
    return edges


def solve():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    islands, island_count = labeling(board, n, m)
    edges = find_bridges(islands, n, m)
    edges.sort()  # 다리 길이 짧은 것부터

    parent = [i for i in range(island_count + 1)]  # 0은 안 씀

    total = 0
    count = 0  # 연결된 간선 수
    for length, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total += length
            count += 1

    # 섬 개수 - 1 만큼 간선이 있어야 모두 연결된 것
    if count == island_count - 1:
        print(total)
    else:
        print(-1)

solve()
