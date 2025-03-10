T = int(input())

# 이동 방향: 상, 하, 좌, 우
row_offset = [-1, 1, 0, 0]
col_offset = [0, 0, -1, 1]

# 터널 구조 (각 숫자가 연결된 방향)
tunnel_types = [
    [],
    [0, 1, 2, 3],  # 상하좌우 연결
    [0, 1],        # 상하 연결
    [2, 3],        # 좌우 연결
    [0, 3],        # 상우 연결
    [1, 3],        # 하우 연결
    [1, 2],        # 하좌 연결
    [0, 2],        # 상좌 연결
]

def explore(row, col, time):
    if time > max_time:
        return

    visited[row][col] = time
    current_tunnel = tunnel_types[grid[row][col]]

    for direction in current_tunnel:
        next_row = row + row_offset[direction]
        next_col = col + col_offset[direction]

        if not (0 <= next_row < rows and 0 <= next_col < cols):
            continue  # 범위 벗어남
        if grid[next_row][next_col] == 0:
            continue  # 터널 없음
        if visited[next_row][next_col] is not None and visited[next_row][next_col] <= time:
            continue  # 이미 더 짧은 시간에 방문한 경우

        opposite_direction = (direction + 2) % 4  # 반대 방향 계산

        if opposite_direction in tunnel_types[grid[next_row][next_col]]:
            explore(next_row, next_col, time + 1)

for test_case in range(1, T + 1):
    rows, cols, start_row, start_col, max_time = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(rows)]
    visited = [[None] * cols for _ in range(rows)]

    explore(start_row, start_col, 1)

    reachable_count = sum(row.count(None) == False for row in visited)
    print(f'#{test_case} {reachable_count}')
