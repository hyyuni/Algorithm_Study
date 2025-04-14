def perm(cnt):
    # check = 0
    if cnt == M:
        if tuple(answer) not in real:
            real.add(tuple(answer))
            print(*answer)
        return
    
    for i in range(N):
        # if check != numbers[i] and not visited[i]:
        if not visited[i]:
            answer.append(numbers[i])
            visited[i] = 1
            # check = numbers[i]
            perm(cnt+1)
            visited[i] = 0
            answer.pop()
        

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()
visited = [0]*N
answer = []
real = set()

perm(0)