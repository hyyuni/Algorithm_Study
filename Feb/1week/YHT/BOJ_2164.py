n=int(input())
a=[]
while n>1:
    for i in range(1,n+1):
        a.append(i)
        n=n-1
print(a)