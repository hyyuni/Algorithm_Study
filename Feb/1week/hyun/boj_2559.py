N, K = map(int, input().split())
temp = list(map(int, input().split()))

prefix_sum = [0] * (N + 1) # 온도의 누적합, 첫번째 누적합을 구하기 위해 앞에 0을 추가한다
ans = [] # K구간 합 저장할 리스트

# 누적 합 구하기
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + temp[i-1]

# 연속되는 K의 합 구하기
for j in range(N-K+1): # K가 2일 때 8번, K가 5일 때 5번
    temp_sum = prefix_sum[j+K] - prefix_sum[j]
    ans.append(temp_sum)

print(max(ans))
