# 색종이
N = int(input()) # 색종이 수
graph = [[0]*1001 for _ in range(1001)]
area = []
for i in range(1, N+1):
    x1, y1, w, h = map(int, input().split())
    for j in range(h):
        for k in range(w):
            graph[y1+j][x1+k] = i

for k in range(1, N+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if graph[i][j] == k:
                cnt += 1
    area.append(cnt)

for i in range(len(area)):
    print(area[i])

