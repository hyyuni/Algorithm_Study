T=int(input())
for i in range(1,T+1):
    N,M=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(N)]
    max2=0
    for k in range(N-M+1):
        for j in range(N-M+1):
            sum=0
            for x in range(M):
                for y in range(M):
                    sum+=a[x+k][y+j]
                    max2=max(max2,sum)
    print(f'#{i} {max2}')
