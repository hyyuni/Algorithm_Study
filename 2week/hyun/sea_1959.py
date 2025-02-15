T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = []

    if N <= M: # N이 M보다 작거나 같다면
        for i in range(M-N+1): # A는 M-N+1만큼 이동 가능 
            temp = 0
            for j in range(N): # 이동했을 때 마주보는 값 곱하기
                temp += A[j] * B[j+i]
            ans.append(temp) # 값 정답 리스트에 넣어주기
    else: # N이 M보다 크다면
        for i in range(N-M+1):
            temp = 0
            for j in range(M):
                temp += B[j] * A[j+i]
            ans.append(temp)

    max_ans = max(ans)

    print(f'#{tc} {max_ans}')