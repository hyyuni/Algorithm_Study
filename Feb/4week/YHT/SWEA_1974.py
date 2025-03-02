T=int(input())
for i in range(1,T+1):
    a=[list(map(int,input().split())) for _ in range(9)]
    c=0
    f=0
    v=[]
    b=[]
    e=[]
    for x in range(9):
        b.append(set(a[x]))
        if(len(b[x])==9):
            c+=1
    d=list(map(list,zip(*a)))
    for x in range(9):
        
        e.append(set(d[x]))
        if(len(e[x])==9):
            f+=1
    zm=0
    for k in range(3):
        for w in range(3):
            s=[]
            for x in range(3):
                for y in range(3):
                    v.append(a[x+k+w][y+k+w])
            s=set(v)
            if(len(s)==9):
                zm+=1
    print(f'#{i}',end=" ")
    if(c==9 and f==9 and zm==9):
        print(1)
    else:
        print(0)
