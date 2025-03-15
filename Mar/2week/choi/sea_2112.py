T = int(input())

def check_conti(arr):
    for col in range(W):
        cnt = 1
        before = arr[0][col]
        for row in range(1, D): 
            if arr[row][col] == before:
                cnt += 1
                if cnt >= K:
                    break
            else:
                cnt = 1
                before = arr[row][col]
        if cnt < K:
            return 0
    return 1

def dfs(arr, idx, change):
    global result

    if change >= result:
        return
    if check_conti(arr):
        result = min(result, change)
        return

    if idx == D:
        return
    
    backup_row = arr[idx]

    arr[idx] = [0] * W
    dfs(arr, idx + 1, change + 1)

    arr[idx] = [1] * W
    dfs(arr, idx + 1, change + 1)
    
    arr[idx] = backup_row
    dfs(arr, idx + 1, change)
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    result = K
    dfs(arr, 0, 0)

    print(f'#{tc} {result}')
