# 치킨 배달
from itertools import combinations

def calculate_cd(h, c): # 치킨 거리 계산 함수
    tot_cd = 0
    for i in range(len(h)):
        min_cd = 21e8
        r1, c1 = h[i]
        for j in range(len(c)):
            r2, c2 = c[j]
            cd = abs(r1 - r2) + abs(c1 - c2)
            if min_cd > cd:
                min_cd = cd
        tot_cd += min_cd
    return tot_cd

n, m = map(int, input().split())
chicken_map = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if chicken_map[i][j] == 1:
            house.append((i, j))
        if chicken_map[i][j] == 2:
            chicken.append((i, j))
min_distance = 21e8
if len(chicken) > m:
    for chick in combinations(chicken, m):
        closed = calculate_cd(house, chick)
        min_distance = min(min_distance, closed)
else:
    min_distance = calculate_cd(house, chicken)

print(min_distance)



