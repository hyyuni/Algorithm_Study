import sys
input = sys.stdin.readline

def dfs(n, sum):
    global ans

    if ans <= sum-B: # 최솟값을 이미 넘었다면 가지치기
        return
    
    if n == N: # n 값이 N과 같아진다면 dfs 종료
        if sum >= B:
            ans = min(ans, sum-B)
        return

    # 이진트리 형태 dfs    
    dfs(n+1, sum+lst[n])
    dfs(n+1, sum)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = float('inf')
    dfs(0, 0)

    print(f'#{tc} {ans}')