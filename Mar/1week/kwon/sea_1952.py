# 수영장
def dfs(m, c):
    global result
    if m >= 12:
        result = min(result, c)
        return
    # 1일 vs 1달
    dfs(m + 1, c + min(plans[m] * fee[0], fee[1]))

    # 3달
    if m <= 9:
        dfs(m + 3, c + fee[2])

    # 1년
    if m == 0:
        dfs(12, c + fee[3])


T = int(input())
for tc in range(1, T + 1):
    fee = list(map(int, input().split()))
    plans = list(map(int, input().split()))

    result = fee[3]
    dfs(0, 0)

    print(f'#{tc} {result}')