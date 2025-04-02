# 아~파트 아파트 S4
N, M = map(int, input().split())
hands = [0] * (2 * M)

for i in range(M):
    L, R = map(int, input().split())
    hands[L-1] = i + 1
    hands[R-1] = i + 1

if N <= 2 * M:
    ans = hands[N-1]
else:
    k = N % (2 * M)
    if k == 0:
        ans = hands[0]
    else:
        ans = hands[k-1]
print(ans)