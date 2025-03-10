from itertools import product
from itertools import permutations
from collections import deque
from copy import deepcopy

def turn(c):
    ar = [0, 1, 2, 3]
    for i in product(ar, repeat=5):
        idx = 0
        made = []
        for j in i:
            b = list(zip(*c[idx][::-1]))
            d = list(zip(*b[::-1]))
            e = list(zip(*d[::-1]))
            if j == 0:
                made.append(c[idx])
            elif j == 1:
                made.append(b)
            elif j == 2:
                made.append(d)
            else:
                made.append(e)
            idx += 1
        bfs(made)


def bfs(cu):
    global answer
    q = deque()
    visited = [[[0, 0, 0, 0, 0] for _ in range(5)] for _ in range(5)]
    if cu[0][0][0] == 1 and cu[4][4][4] == 1:
        q.append((0, 0, 0, 0))
        visited[0][0][0] = 1
        while q:
            cnt = 0
            z, x, y, cnt = q.popleft()
            if z == x == y == 4:
                answer = min(answer,cnt)
                return
            for dir in range(6):
                nz, nx, ny = dz[dir] + z, dx[dir] + x, dy[dir] + y
                if 0 <= nz < 5 and 0 <= nx < 5 and 0 <= ny < 5:
                    if cu[nz][nx][ny] == 1 and visited[nz][nx][ny] == 0:
                        visited[nz][nx][ny] = 1
                        q.append((nz, nx, ny, cnt+1))

answer = float('inf')
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

arr = []


for i in range(5):
    arr1 = [list(map(int, input().split())) for _ in range(5)]
    arr.append(arr1)

for cube in permutations(arr, 5):
    turn(cube)

if answer == float('inf'):
    print(-1)
else:
    print(answer)
