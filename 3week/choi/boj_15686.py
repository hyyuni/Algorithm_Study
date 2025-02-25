import sys
input = sys.stdin.read

def calculate_chicken_distance(houses, selected_chickens):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in selected_chickens:
            distance = abs(hx - cx) + abs(hy - cy)
            if distance < min_distance:
                min_distance = distance
        total_distance += min_distance
    return total_distance

def dfs(idx, selected):
    global min_city_distance
    if len(selected) == M:
        min_city_distance = min(min_city_distance, calculate_chicken_distance(houses, selected))
        return
    if idx >= len(chickens):
        return
    dfs(idx + 1, selected + [chickens[idx]])
    dfs(idx + 1, selected)

data = input().splitlines()
N, M = map(int, data[0].split())
city_map = [list(map(int, line.split())) for line in data[1:N+1]]

houses = []
chickens = []
for r in range(N):
    for c in range(N):
        if city_map[r][c] == 1:
            houses.append((r, c))
        elif city_map[r][c] == 2:
            chickens.append((r, c))

min_city_distance = float('inf')
dfs(0, [])
print(min_city_distance)
