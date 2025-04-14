def comb2(idx,cnt):
    if cnt == M:
        print(*answer)
        return
    for i in range(idx,N+1):
        answer.append(i)
        comb2(i,cnt+1)
        answer.pop()

N, M = map(int,input().split())
answer = []
comb2(1,0)