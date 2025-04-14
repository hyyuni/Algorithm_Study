def perm(cnt):
    if cnt == M:
        print(*answer)
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = 1
            answer.append(i)
            perm(cnt+1)
            answer.pop()
            visited[i] = 0
N, M = map(int,input().split())
visited = [0]*(N+1)
answer = []

perm(0)