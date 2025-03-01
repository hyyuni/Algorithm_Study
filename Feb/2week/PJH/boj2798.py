N,M = map(int,input().split())
black = list(map(int,input().split()))
# 블랙잭 카드 뽑은 조합
ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if ans < black[i] +black[j]+black[k]<=M:
                ans = black[i] +black[j]+black[k]
print(ans)



    
