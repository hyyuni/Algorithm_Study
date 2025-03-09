import sys
input = sys.stdin.readline

import heapq

INF = float('inf')

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)] #그래프 만들기
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF] * (V + 1) #다익스트라 준비
distance[K] = 0

heap = []
heapq.heappush(heap, (0, K))  
# (시작 정점까지의 거리, 시작 정점) 형태로 넣기

while heap:
    cur_dist, cur_node = heapq.heappop(heap)

    # 이미 더 짧은 경로를 찾았다면 스킵
    if distance[cur_node] < cur_dist:
        continue

    # 인접 정점 확인
    for next_node, weight in graph[cur_node]:
        cost = cur_dist + weight
        # 더 짧은 경로 발견 시 갱신
        if distance[next_node] > cost:
            distance[next_node] = cost
            heapq.heappush(heap, (cost, next_node))



for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
        continue
    print(distance[i])