def perm2(cnt):
    if cnt == M:
        print(*answer)
        return
    for i in range(N):
        answer.append(numbers[i])
        perm2(cnt+1)
        answer.pop()

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
answer = []
numbers.sort()
perm2(0)