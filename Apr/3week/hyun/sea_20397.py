T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1
        for k in range(1,j+1):
            left = i - k
            right = i + k
        
            if left < 0 or right >= N:
                continue
            
            if arr[left] == arr[right]:
                arr[left] = 1 - arr[left]
                arr[right] = 1 - arr[right]

    print(f'#{tc}', *arr)