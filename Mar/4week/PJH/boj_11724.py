def dfs(v):
    visited[v] = 1
    for i in range(1,N+1):
        if adj[v][i] == 1 and visited[i] == 0:
            dfs(i)

N, M = map(int,input().split())
adj = [[0]*(N+1) for _ in range(N+1)]
for m in range(M):
    i, j = map(int,input().split())
    adj[i][j] = 1
    adj[j][i] = 1
visited = [0]*(N+1)
ans = 0
for v in range(1,N+1):
    if visited[v] == 0:
        dfs(v)
        ans += 1

print(ans)