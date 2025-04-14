def comb(idx,cnt):
    if cnt == M:
        print(*answer)
        return
    
    for i in range(idx,N+1):
            answer.append(i)
            comb(i+1,cnt+1)
            answer.pop()


N , M = map(int,input().split())
answer = []
comb(1,0)
