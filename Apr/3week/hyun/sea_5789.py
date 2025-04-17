T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0]*(N+1)
    for i in range(1,M+1):
        L, R = map(int, input().split())
        for j in range(L,R+1):
            arr[j] = i
    ans = arr[1:]
    print(f'#{tc}', *ans)