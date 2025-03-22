def dfs(idx, cal):
    global max_v, min_v
    
    if idx == N:
        max_v = max(max_v, cal)
        min_v = min(min_v, cal)
        return

    for i in range(4):
        if operators[i] > 0:  # 해당 연산자가 남아있는 경우
            operators[i] -= 1         
            if i == 0:  # '+'
                dfs(idx + 1, cal + nums[idx])
            elif i == 1:  # '-'
                dfs(idx + 1, cal - nums[idx])
            elif i == 2:  # '*'
                dfs(idx + 1, cal * nums[idx])
            elif i == 3:  # '/'
                dfs(idx + 1, int(cal / nums[idx]))
            operators[i] += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    operators = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    max_v = -float('inf')
    min_v = float('inf')
    
    dfs(1, nums[0]) # 연산은 수행은 처음값이 이미 있어야 하므로 0이아닌 1부터 dfs
    ans = max_v - min_v

    print(f"#{tc} {ans}")