from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        for near in graph[node]:
            if near not in visited:
                visited.add(near)
                queue.append(near)
    
    return len(visited) - 1
n = int(input()) 
m = int(input())

graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph, 1))
