# 4를 나타내기 -> 총 7개
# 방법     4되기 전 마지막 합
# 1+1+1+1  3 
# 1+1+2    2
# 1+2+1    3
# 2+1+1    3
# 2+2      2
# 1+3      1
# 3+1      3

# 3을 나타내기 -> 총 4개
# 1+1+1
    # +1
# 1+2
    # +1
# 2+1
    # + 1
# 3
#   + 1

# 2를 나타내기 -> 총 2개
# 1+1
# 2

# 1을 나타내기 -> 총 1개
# 1

import sys
T = int(input())
for t in range(T):
    n = int(input())
    dp = [0] * (n + 1)
    for i in range(1, n+1):
        if i == 1 or i == 2:
            dp[i] = i
            continue
        elif i == 3:
            dp[i] = 4
            continue
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])