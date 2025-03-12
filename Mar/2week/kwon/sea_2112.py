# 보호 필름
def testfilm(arr):
    for c in range(w):
        cnt = 1
        for r in range(d-1):
            if arr[r][c] == arr[r+1][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= k: # 동일 특성이 k개 이상
                break
        if cnt < k:
            return False
    return True

def comb(depth, count, pick):
    global result
    # 주입 횟수가 최소 약품 주입 횟수보다 크거나 같으면
    if count >= result: # 가지치기
        return

    if count == pick: # pick 횟수에 도달하면 검사
        if testfilm(film):
            result = min(result, pick)
        return

    if depth >= d: # 약물 투입 깊이가 d를 넘으면
        return

    temp = film[depth]
    # 약물 투입 X
    comb(depth+1, count, pick)
    # 약물A 투입
    film[depth] = [0] * w
    comb(depth+1, count+1, pick)
    # 약물B 투입
    film[depth] = [1] * w
    comb(depth + 1, count + 1, pick)

    film[depth] = temp

T = int(input())
for tc in range(1, T+1):
    d, w, k = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(d)]
    result = k # k가 최대이므로

    if testfilm(film): # 약물 투입이 필요 없을 경우
        result = 0
    else:
        for pick in range(1, d+1):
            comb(0, 0, pick)

            if result < k:
                break

    print(f'#{tc} {result}')

