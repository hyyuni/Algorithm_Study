T, W = map(int, input().split())

dp = [[0]*(W+1) for _ in range(T+1)]
arr = list(int(input()) for _ in range(T))
arr.insert(0,0)

for i in range(1, T+1):
    if arr[i] == 1:
        dp[i][0] = dp[i-1][0]+1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, W+1):
        if arr[i] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        elif arr[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) 

print(max(dp[-1]))

