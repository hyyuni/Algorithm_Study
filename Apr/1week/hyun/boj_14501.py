# SWEA의 수영장과 유사한 문제 백트래킹, 그리디 모두 가능

# 2. 그리디 접근
# dp[i] = i번째 상담 결정 시의 최대 수익(Tip, 거꾸로 누적합 기록)

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0]*(N+1) # 여기서 dp[N]은 참조용으로 필요해서 (상담이 끝났을 때, 0 처리)

for time in range(N-1, -1, -1):
    if time+T[time]<=N:
        dp[time] = max(dp[time+1], dp[time+T[time]]+P[time])
    else:
        dp[time] = dp[time+1]

print(dp[0])

'''
1. dfs 백트래킹 풀이
재귀 호출로 완탐해도 2^15이기 때문에 가능 (2^50가 이진트리에서 마지노선 recurursion maximum)

def dfs(time, cost):
    global ans
    if time >= N:
        ans = max(ans, cost)
        return

    # 상담을 하는 경우
    if time+T[time]<=N:
        dfs(time+T[time], cost+P[time])
    
    # 상담을 하지 않는 경우
    dfs(time+1, cost)


N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

ans = 0
dfs(0,0)

print(ans)
'''