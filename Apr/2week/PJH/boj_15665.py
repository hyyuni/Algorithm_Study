def perm2(cnt):
    check = 0
    if cnt == M:
        print(*answer)
        return

    for i in range(N):
        if check != numbers[i]:
            answer.append(numbers[i])
            check = numbers[i]
            perm2(cnt+1)
            answer.pop()

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()
answer = []

perm2(0)