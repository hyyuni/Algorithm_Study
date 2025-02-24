T=int(input())
for i in range(1,T+1):
    n=int(input())
    a=[[-1]*(n) for _ in range(n)]
    count=1
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
  
    x=0
    y=0
    a[x][y]=count
    count+=1
    dr=0
    while count<=n*n:
        nx,ny=x+dx[dr],y+dy[dr]
        if(0<=nx<n and 0<=ny<n and a[nx][ny]==-1):
            x,y=nx,ny
            a[x][y]=count
            count+=1
        else:
            dr=(dr+1)%4


    print(f'#{i}')
    for x in range(n):
        for y in range(n):
            
            print(a[x][y],end=" ")
        print()