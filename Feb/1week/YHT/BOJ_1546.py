n=int(input())
a=list(map(int,input().split()))
a.sort()
for i in range(0,n):
    a[i]=100*((a[i])/(a[-1]))
print(sum(a)/len(a))
