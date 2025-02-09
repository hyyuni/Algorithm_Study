"""
1.스위치 개수 받기
스위치 상태 
성별 받은수
성별과 받은수에 따라 스위치 상태 바꿀떄 마지막 상태

"""

n=int(input())
a=list(map(int,input().split()))
b=int(input())
c,d=map(int,input().split())
e,f=map(int,input().split())
result=[]
for i in range(0,n):
    j=n//c
    iter=c*(j-i)-1
    if(iter>=0):
        if(c==1 and a[iter]==0):
            a[iter]=1
        elif(c==1 and a[iter]==1):
            a[iter]=0

    # if(iter>=0):
    #   if(b[0] and a[iter]==1):
    #         a[iter]=0
    #   elif(b==1 and a[iter]==0):
    #         a[iter]=1
    
print(a)
