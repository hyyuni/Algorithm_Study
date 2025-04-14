def comb2(idx,cnt):
    check = 0
    if cnt == M:
        print(*answer)
        return

    for i in range(idx,N):
        if check != numbers[i]:
            answer.append(numbers[i])
            check = numbers[i]
            comb2(i,cnt+1)
            answer.pop()    
    

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()
answer = []

comb2(0,0)
