T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))


    for _ in range(M):
        i, j = map(int, input().split())
        # 변수 설정, 왼쪽 = l / 오른쪽 = r
        i -= 1 # 인덱싱은 0부터 시작하므로 조정
        for k in range(1, j+1):
            left = i - k
            right = i + k
            if left < 0 or right >= N: # 인덱스 범위 벗어나면
                break
            if stones[left] == stones[right]:
                stones[left] = 1 - stones[left]
                stones[right] = 1 - stones[right]
    print(f'#{tc} {" ".join(map(str, stones))}') # join을 쓰기 위해 int -> str

