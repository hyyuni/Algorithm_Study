# 순열 사이클
def dfs(v):
    visited[v] = 1
    next = arr[v]
    if visited[next] == 0:
        dfs(next)
    return 

tc = int(input())
for _ in range(tc):
    N = int(input())
    arr = [0] + list(map(int,input().split()))
    visited = [0]*(N+1)
    cnt = 0 

    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            cnt += 1
    print(cnt)


