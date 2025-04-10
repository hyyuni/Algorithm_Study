from heapq import heappop, heappush

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)] 

for i in range(M):
    s, e = map(int,input().split())
    graph[s].append((e,i))
    graph[e].append((s,i))


def dijkstra(graph, start, end):
    times = [float('inf') for _ in range(N+1)]
    times[start] = 0
    hq = [(0, start)]

    while hq:
        cur_time, cur_node = heappop(hq)

        if cur_node == end:
            return cur_time

        if cur_time > times[cur_node]:
            continue

        for next_node, next_remain_time in graph[cur_node]:
            wait = (next_remain_time - (cur_time % M)) % M
            next_time = cur_time + wait + 1

            if next_time < times[next_node]:
                times[next_node] = next_time
                heappush(hq, (next_time, next_node))
    
    return -1


print(dijkstra(graph, 1, N))