L = int(input())
N = int(input())
lst = [1] * (L+1)
max1 = max2 = 0
idx_1 = idx_2 = 0

for i in range(1, N+1): # 방청객의 수만큼 반복
    s, e = map(int, input().split())
    if max1 < (e-s+1): # 롤케익을 원한 개수가 가장 큰 값이면 갱신하기
        max1, idx_1 = (e-s+1), i
    
    # i 방청객이 받은 롤케익의 개수
    cnt = sum(lst[s:e+1]) 
    if max2 < cnt:
        max2, idx_2 = cnt, i
    # 롤 케익을 가져갔다면 개수를 0으로 처리하기    
    lst[s:e+1] = [0] * (e-s+1) 

print(idx_1)
print(idx_2)