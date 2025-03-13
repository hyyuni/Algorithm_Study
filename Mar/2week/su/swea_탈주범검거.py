def solve_escape_simulation():
    test_cases = int(input())
     
    directions = {
        'up': 0,
        'down': 1,
        'left': 2,
        'right': 3
    }
     
    tunnel_types = [
        [],  # 빈 공간
        [directions['up'], directions['down'], directions['left'], directions['right']],  # 1번 터널
        [directions['up'], directions['down']],  # 2
        [directions['left'], directions['right']],  # 3
        [directions['up'], directions['right']],  # 4
        [directions['down'], directions['right']],  # 5
        [directions['down'], directions['left']],  # 6
        [directions['up'], directions['left']]  # 7
    ]
     
    direction_row = [-1, 1, 0, 0]  
    direction_col = [0, 0, -1, 1]  
     
    opposite_direction = {
        directions['up']: directions['down'],
        directions['down']: directions['up'],
        directions['left']: directions['right'],
        directions['right']: directions['left']
    }
     
    def dfs(row, col, elapsed_time):
        """
        깊이 우선 탐색으로 탈주범이 이동할 수 있는 위치를 탐색
        """
        if elapsed_time > time_limit:
            return
         
        time_map[row][col] = elapsed_time
         
        available_directions = tunnel_types[tunnel_map[row][col]]
         
        for direction in available_directions:
            next_row = row + direction_row[direction]
            next_col = col + direction_col[direction]
             
             
            if (next_row < 0 or next_row >= height or 
                next_col < 0 or next_col >= width or 
                tunnel_map[next_row][next_col] == 0):
                continue
             
            # 아직 방문하지 않았거나 더 빠른 시간에 방문할 수 있는 경우
            if time_map[next_row][next_col] == 0 or time_map[next_row][next_col] > elapsed_time + 1:
                next_direction = opposite_direction[direction]
                 
                # 다음 위치의 터널이 현재 위치와 연결 가능한 경우 이동
                if next_direction in tunnel_types[tunnel_map[next_row][next_col]]:
                    dfs(next_row, next_col, elapsed_time + 1)
     
    for tc in range(1, test_cases + 1):
        height, width, start_row, start_col, time_limit = map(int, input().split())
         
         
        tunnel_map = [list(map(int, input().split())) for _ in range(height)]
         
         
        time_map = [[0] * width for _ in range(height)]
         
         
        dfs(start_row, start_col, 1)
         
         
        accessible_locations = 0
        for row in range(height):
            for col in range(width):
                if time_map[row][col] > 0:
                    accessible_locations += 1
         
        print(f'#{tc} {accessible_locations}')
 
solve_escape_simulation()