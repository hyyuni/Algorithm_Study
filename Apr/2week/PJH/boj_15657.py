def comb2(idx,cnt):
    if cnt == M:
        print(*answer)
        return
    
    for i in range(idx,N):
        answer.append(numbers[i])
        comb2(i,cnt+1)
        answer.pop()

N,M = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()
answer = []
comb2(0,0)