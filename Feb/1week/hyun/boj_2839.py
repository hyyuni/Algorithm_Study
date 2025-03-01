N = int(input())

if N % 5 == 0: # 설탕봉지가 5kg으로 나눠 떨어질 때
    print(N//5)
else:
    ans = 0
    while N > 0: # 설탕봉지가 5kg과 3kg으로 나눠질 때
        N -= 3 # N//3을 하면 더 많은 경우의 수가 나오므로 5kg으로 나눠질 때까지 하나씩 제외
        ans += 1 
        if N % 5 == 0:
            ans += N // 5
            print(ans)
            break
        elif N == 1 or N == 2: # 5, 3kg으로 나누지 못하는 경우
            print(-1)
            break
        elif N == 0: # N이 0이 될 때까지 5kg으로 나눠지지 않는다면
            print(ans)
        