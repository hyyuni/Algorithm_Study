import sys
sys.stdin = open('input.txt', 'r')
import heapq

def dijkstra(start):
    INF = float('inf')
    distance = [INF]*(N+1)
    distance[start] = 0

    pq = [(0,start)] # (비용, 시작 노드)

    while pq:
        cost, node = heapq.heappop(pq)

        # 저장된 최단 거리보다 큰 비용이라면 무시하기
        if distance[node] < cost:
            continue
        
        # 인접한 노드 탐색
        for next_cost, next_node in graph[node]:
            memo = cost + next_cost

            # 새로운 경로가 저장된 경로보다 비용이 적다면 업데이트하기
            if memo < distance[next_node]:
                distance[next_node] = memo
                heapq.heappush(pq, (memo, next_node))
    
    return distance

N = int(input())
M = int(input())

# 인접 리스트
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, weight = map(int, input().split())
    graph[s].append((weight,e)) # (가중치, 도착점)

start, end = map(int, input().split())

# 다익스트라 실행
distance = dijkstra(start)

# 시작점에서 도착점까지의 최단 거리
ans = distance[end]

print(ans)