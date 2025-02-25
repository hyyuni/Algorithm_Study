# 파리 퇴치
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    max_sum = 0 # 최대 합

    #행렬 입력
    mat = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N-M+1):
        for j in range(N-M+1):
            mat_sum = 0 # 부분합 초기화
            for m in range(M): # MxM 부분합 구하기
                for n in range(M):
                    mat_sum += mat[i + m][j + n]
            if max_sum < mat_sum:
                max_sum = mat_sum
    print(f'#{tc} {max_sum}')