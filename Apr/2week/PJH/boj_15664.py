def comb(idx,cnt):
    check = 0
    if cnt == M:
        print(*answer)

    for i in range(idx,N):
        if check != numbers[i]:
            answer.append(numbers[i])
            check = numbers[i]
            comb(i+1,cnt+1)
            answer.pop()

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()
answer = []

comb(0,0)