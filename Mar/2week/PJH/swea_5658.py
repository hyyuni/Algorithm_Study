T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    password = list(input())
    sixteen = [[] for _ in range(N//4)]
    new_p = password
    for r in range(N//4):
        for i in range(0,N,N//4):
            sixteen[r].append(''.join(new_p[i:i+(N//4)]))
        new_p = [0]*N
        for i in range(N):
            new_p[i] = password[((i+12)-(r+1))%12]
    answer = []
    for s in sixteen:
        answer += s
    answer = list(set(answer))
    for i in range(len(answer)):
        answer[i] = int(answer[i],16)
    answer = sorted(answer,reverse=True)
    print(sixteen)
    print(answer)
    print(f'#{tc} {answer[K-1]}')
        



            
