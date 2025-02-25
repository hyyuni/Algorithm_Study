T=1
for i in range(1,T+1):
    i=int(input())
    a=list(map(int,input().split()))
    count2=[]
    max2=0
    for x in range(1000):
        count2.append(a.count(x))
    for x in range(1000):
        max2=max(count2)
        if(max2==count2[x]):
            v=i
    print(f'#{i} {a[v]}')
