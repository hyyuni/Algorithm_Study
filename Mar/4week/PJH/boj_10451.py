def dfs(idx):
    visited[idx] = 1
    for j in range(N+1):
        if adj[idx][j] == 1 and visited[j] == 0:
            dfs(j)
            break

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    perm = [0]+list(map(int,input().split()))
    adj = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        adj[i][perm[i]] = 1
    visited = [0]*(N+1)
    cnt = 0
    for i in range(1,N+1):
        if visited[i] == 0:
            cnt += 1
            # print(i)
            dfs(i)
    print(cnt)