import heapq
import math

def calc(s,e):
    x1, y1 = gods[s]
    x2, y2 = gods[e]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def marking(v):
    visited[v] = True
    for u in connected[v]:
        if not visited[u]:
            marking(u)
    for i in range(V):
        if not visited[i]:
            dist = calc(v, i)
            heapq.heappush(pq, (dist, i))

def prim(start):
    res = 0.0
    marking(start)
    while pq:
        cost, node = heapq.heappop(pq)
        if not visited[node]:
            res += cost
            marking(node)
    return res


V, E = map(int, input().split())
gods = [tuple(map(float, input().split())) for _ in range(V)]

# 이미 연결된 간선(통로) 정보 처리하기
connected = [[] for _ in range(V)]
for _ in range(E):
    a, b = map(int, input().split())
    connected[a-1].append(b-1)
    connected[b-1].append(a-1)

visited = [False]*V
pq = []
ans = prim(0)

print(f'{ans:.2f}')