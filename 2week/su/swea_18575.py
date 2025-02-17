T = int(input())
 
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
 
    max_val = -1
    min_val = int(1e9)
    zipped = list(zip(*arr))
    row_sum = [0] * N
    col_sum = [0] * N
    for i in range(N):
        row_sum[i] = sum(arr[i])
        col_sum[i] = sum(zipped[i])
 
    for i in range(N):
        for j in range(N):
            cur = row_sum[i] + col_sum[j] - arr[i][j]
            min_val = min(min_val, cur)
            max_val = max(max_val, cur)
 
    print(f"#{t} {max_val - min_val}")