# 색종이 S5

N = int(input())
graph = [[0] * 100 for _ in range(100)]
cnt = 0

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            graph[i][j] = 1

for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            cnt += 1

print(cnt)