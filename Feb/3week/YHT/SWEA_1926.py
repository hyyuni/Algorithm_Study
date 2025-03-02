n=int(input())
re=[]

for i in range(n):
    re.append(str(i+1))
for i in range(n):
    count2=0
    if('3' in re[i] or '6' in re[i] or '9' in re[i]):
        count2+=re[i].count('3')+re[i].count('6')+re[i].count('9')
        print('-'*count2,end=" ")
    else:
        print(i+1,end=" ")