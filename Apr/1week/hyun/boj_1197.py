import heapq

V, E = map(int, input().split())

def prim(start):
    visited = [False]*(V+1)
    pq = [(0,start)]
    total = 0

    while pq:
        weight, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True
        total += weight

        for next_info in graph[u]:
            next_weight, v = next_info
            if not visited[v]:
                heapq.heappush(pq, (next_weight, v))

    return total

graph = [[] for _ in range(V+1)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((weight,end))
    graph[end].append((weight,start))


ans = prim(1)

print(ans)