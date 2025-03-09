t=int(input())
for i in range(1,t+1):
    a,b=map(int,input().split())
    c=[list(map(int,input().split())) for _ in range(2)]
    re=[]
    realre=[]
    if(a>b):
        a,b=b,a
        c[0],c[1]=c[1],c[0]
    for w in range(b-a+1):
        sum=0
        for j in range(1):
            for k in range(a):
                sum+=(c[j][k]*c[j+1][k+w])
        re.append(sum)
    print(f'#{i} {max(re)}')