import heapq
 
INF = int(1e9)
T = int(input())
 
def prim(start_node):
    pq = [(0, start_node)]  # cost, node
    MST = [0] * N
    min_cost = 0  # 최소 비용 계속 저장할 예정
    # heapq.heapify(pq)
     
    while pq:
        cost, node = heapq.heappop(pq)
        if MST[node]:  # 이미 방문한 노드인 경우
            continue
         
        MST[node] = 1  # 방문 처리
        min_cost += cost
 
        for next_node in range(N):
            # if graph[node][next_node] == 0:
            #     continue
            if MST[next_node]:
                continue
            heapq.heappush(pq, (graph[node][next_node], next_node))
         
    return min_cost
 
for tc in range(1, T + 1):
    answer = 0
    N = int(input())
    graph = [[INF] * N for _ in range(N)]
    pos_x = list(map(int, input().split()))
    pos_y = list(map(int, input().split()))
    E = float(input())
 
    for i in range(N):
        for j in range(N):
            if i == j:
                graph[i][j] = 0
                continue
            ix, iy = pos_x[i], pos_y[i] 
            jx, jy = pos_x[j], pos_y[j] 
            dist = (ix - jx)**2 + (iy - jy)**2
            graph[i][j] = E * dist
            graph[j][i] = E * dist
     
    answer = round(prim(0))
 
    print(f"#{tc} {answer}")