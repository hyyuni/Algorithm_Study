import itertools

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
EMPTY, HOME, CHICKEN = 0, 1, 2
h_cnt = 0
h_li = []

chickens = []
chicken_cnt = 0
answer = int(1e9)

for i in range(N):
    for j in range(N):
        if graph[i][j] == HOME:
            h_cnt += 1
            h_li.append((i, j))
        elif graph[i][j] == CHICKEN:
            chickens.append((i, j))
            chicken_cnt += 1

distances = [[0] * chicken_cnt for _ in range(h_cnt)]
for i in range(h_cnt):
    for j in range(chicken_cnt):
        distances[i][j] = abs(h_li[i][0] - chickens[j][0]) + abs(h_li[i][1] - chickens[j][1])


li = [i for i in range(chicken_cnt)]
for survived in itertools.combinations([i for i in range(chicken_cnt)], M):
    result = 0
    for h in range(h_cnt):
        temp = int(1e9)
        for chicken_idx in survived: # (0, 1) 이런식
            if temp > distances[h][chicken_idx]:
                temp = distances[h][chicken_idx]
        result += temp
    answer = min(answer, result)
print(answer)
