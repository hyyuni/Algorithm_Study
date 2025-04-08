import heapq

# 라이브 강의 때 금기륜 강사님이 알려주신, key를 이용해 prim 최적화 하는 방법
def prim(start):
    visited = [False]*N
    key = [float('inf')]*N
    key[start] = 0
    pq = [(0, start)]
    min_cost = 0

    while pq:
        cost, u = heapq.heappop(pq)
        
        if visited[u]:
            continue

        visited[u] = True
        min_cost += cost

        for next_cost, v in edges[u]:
            # key를 이용한 최적화
            if not visited[v] and next_cost < key[v]:
                key[v] = next_cost
                heapq.heappush(pq, (next_cost, v))

    return min_cost

N = int(input())

planets = []

for idx in range(N):
    x, y, z = map(int, input().split())
    planets.append((idx, x, y, z))

# x, y, z 축별 인접 리스트 생성하기
edges = [[] for _ in range(N)]

for idx in range(1, 4): # 행성 번호(idx)에서 x축, y축, z축 별 거리 재기
    planets.sort(key=lambda x: x[idx]) # 각 축마다 정렬하기 위해 lambda 사용
    for i in range(N-1): # N이 1이더라도 prim은 정상적으로 작동해서 0 출력 됨
        start, end = planets[i][0], planets[i+1][0]
        weight = abs(planets[i][idx] - planets[i+1][idx])
        edges[start].append((weight, end))
        edges[end].append((weight, start))

ans = prim(0)

print(ans)