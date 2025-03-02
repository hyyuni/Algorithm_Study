

def bfs(graph, v, visited):
    queue = [v]
    visited[v] = True
    while queue:
        a = queue.pop(0)
        print(a, end= " ")
        for i in sorted(graph[a]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)






N, M, V = map(int,input().split())


arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)



visited = [False] * (N + 1)
dfs(arr,V,visited)
print()
visited = [False] * (N + 1)
bfs(arr, V, visited)