from itertools import combinations
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cook = [list(map(int,input().split())) for _ in range(N)]
    # N개의 재료 N//2개로 나눠주기
    min_v = 40000
    for c in combinations(list(range(N)),N//2):
        c_a = set(range(N)) - set(c)
        for ca in combinations(list(c),2):
            i_a,j_a = ca
        for cb in combinations(list(c_a),2):
            i_b,j_b = cb
        ans_a = cook[i_a][j_a]
        ans_b = cook[i_b][j_b]
        ans = abs(ans_a-ans_b)
        if ans<min_v:
            min_v = ans
    print(f'#{tc} {min_v}')