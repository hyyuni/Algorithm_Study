import sys
sys.stdin = open('input.txt', 'r')
import heapq
import math

def prim(N, stars):
    for s1 in range(N):
        for s2 in range(s1+1, N):
            # 일타싸피에서 익힌 sqrt 활용! 두 점 사이의 거리? x,y 좌표를 통한 피타고라스 정리!
            dist = math.sqrt((stars[s1][0] - stars[s2][0])**2 + (stars[s1][1] - stars[s2][1])**2)
            graph[s1].append((dist, s2))
            graph[s2].append((dist, s1))
    
    visited = [False] * N
    hq = [(0, 0)]  # (거리, 노드) 거리에 의한 최소 비용이므로 거리가 우선순위
    total_cost = 0
    
    while hq:
        cost, u = heapq.heappop(hq)
        
        # 이미 방문한 노드는 건너뜀
        if visited[u]:
            continue
        
        # 현재 노드 방문 처리 및 비용 추가
        visited[u] = True
        total_cost += cost
        
        # 현재 노드와 연결된 간선들을 힙에 추가
        for next_cost, v in graph[u]:
            if not visited[v]:
                heapq.heappush(hq, (next_cost, v))
    
    return total_cost

N = int(input())
stars = [tuple(map(float, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]

ans = prim(N, stars)
print(f"{ans:.2f}") # 소수점 둘째자리 까지 출력