# 햄버거 다이어트

# 입력 : T, N, L, t, k
# 햄버거 점수 합, 점수 최대값
# 1. 조합 (재귀)

def comb(idx, taste_sum, cal_sum):
    global max_sum

    if cal_sum > L: # 칼로리 제한을 초과하면 종료
        return max_sum
    if max_sum < int(taste_sum):
        max_sum = taste_sum

    for i in range(idx, N):
        comb(i+1,taste_sum + taste[i], cal_sum +cal[i])

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    taste = []
    cal = []
    combi =[]
    max_sum = 0

    for _ in range(N):
        ti, ki = map(int, input().split())
        taste.append(ti)
        cal.append(ki)

    comb(0,0,0)

    print(f'#{tc} {max_sum}')


