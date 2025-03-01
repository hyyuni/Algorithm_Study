T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = {0} #가능한 합의 모든 가능성
    for number in numbers:
        new_sum = {n+number for n in ans}
        ans |= new_sum
    print(f'#{tc} {len(ans)}')