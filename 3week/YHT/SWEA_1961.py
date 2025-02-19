T=int(input())
for i in range(1,T+1):
    
    a=int(input())
    b=[list(map(int,input().split())) for _ in range(a)]
    re=[]
    re=(list(map(list,zip(*b[::-1]))))
    re2=[]
    re2=(list(map(list,zip(*re[::-1]))))
    re3=[]
    re3=(list(map(list,zip(*re2[::-1]))))
    print(f"#{i} ")
    for x in range(a):
        print("".join(map(str,re[x])),"".join(map(str,re2[x])),"".join(map(str,re3[x])))