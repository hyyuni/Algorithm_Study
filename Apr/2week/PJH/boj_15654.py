def perm(cnt):
    if cnt == M:
        print(*answer)
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            answer.append(numbers[i])
            perm(cnt+1)
            visited[i] = 0
            answer.pop()

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()
visited = [0]*N
answer = []
perm(0)