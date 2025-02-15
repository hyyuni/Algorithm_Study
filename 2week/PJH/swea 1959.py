T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: Ai 길이, M: Bi 길이
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    max_v = 0  # 최대 곱 저장 변수 초기화

    if N <= M:
        for i in range(M - N + 1):  # Bi를 기준으로 Ai를 움직이면서 곱 계산
            ans = 0
            for j in range(N):  # Ai 길이만큼 곱 계산
                ans += Ai[j] * Bi[i + j]
            max_v = max(max_v, ans)

    else:
        for i in range(N - M + 1):  # Ai를 기준으로 Bi를 움직이면서 곱 계산
            ans = 0
            for j in range(M):  # Bi 길이만큼 곱 계산
                ans += Ai[i + j] * Bi[j]  # 🔹 `Ai[i + j]`가 N을 초과하지 않도록 `i` 범위 조정
            max_v = max(max_v, ans)

    print(f'#{tc} {max_v}')
