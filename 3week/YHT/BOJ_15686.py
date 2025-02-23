from itertools import combinations as c

def d(a, b):
    return sum(min(abs(x - p) + abs(y - q) for p, q in b) for x, y in a)

n, m = map(int, input().split())  
arr = [list(map(int, input().split())) for _ in range(n)]

a, b = [], []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            a.append((i, j))
        elif arr[i][j] == 2:
            b.append((i, j))

print(min(d(a, x) for x in c(b, m)))