def perm2(cnt):
    if cnt == M:
        print(*answer)
        return
    for i in range(1,N+1):
        answer.append(i)
        perm2(cnt+1)
        answer.pop()

N, M = map(int,input().split())
answer = []
perm2(0)