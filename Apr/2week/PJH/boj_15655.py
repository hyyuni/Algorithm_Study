def comb(idx,cnt):
    if cnt == M:
        print(*answer)
    
    for i in range(idx,N):
        answer.append(numbers[i])
        comb(i+1,cnt+1)
        answer.pop()

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
answer = []
numbers.sort()
comb(0,0)
