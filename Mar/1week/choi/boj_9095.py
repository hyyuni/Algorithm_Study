def dfs(num, sum):
    global cnt
    if num < sum:
        return
    if num == sum:
        cnt += 1
        return
    for i in range(1, 4):
        sum += i
        dfs(num, sum)
        sum -= i
    

result = []

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0

    dfs(N, 0)
    result.append(cnt)

for ans in result:
    print(ans)




T = int(input())
cnt = [0] * 11
cnt[1] = 1
cnt[2] = 2
cnt[3] = 4
for i in range(4, 11):
    cnt[i] = cnt[i-3] + cnt[i-2] + cnt[i-1]
for _ in range(T):
        N = int(input())
        print(cnt[N])