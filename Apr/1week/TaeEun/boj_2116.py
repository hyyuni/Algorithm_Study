
N = int(input())

downs = { 
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
}

dices = [list(map(int, input().split())) for _ in range(N)]

# side_maxes[i][j] : i번째 주사위를 j번 인덱스가 윗면이 되게 놓았을 때의 옆면 최댓값값
side_maxes = [[0]*6 for _ in range(N)]
for i in range(N):
    for top_idx in range(6):
        bottom_idx = downs[top_idx]
        candidates = []
        for face in range(6):
            # 윗면, 아랫면은 제외
            if face != top_idx and face != bottom_idx:
                candidates.append(dices[i][face])
        side_maxes[i][top_idx] = max(candidates)  # 옆면 중 최댓값


dp_next = [0]*6
dp_cur = [0]*6

# 마지막 주사위(N-1)에 대한 dp 초기값 설정
for j in range(6):
    dp_next[j] = side_maxes[N-1][j]

# i=N-2부터 0까지 내려오면서 dp 업데이트
for i in range(N-2, -1, -1):
    for j in range(6):
        # 현재 주사위 i, 윗면=j 일 때 기본 점수
        cur_score = side_maxes[i][j]
        # 다음 주사위와의 매칭(아랫면=현재 윗면 값)
        next_bottom_val = dices[i][j]

        best_next = 0
        # i+1 주사위에서 어떤 k면이 next_bottom_val인지 찾기
        for k in range(6):
            if dices[i+1][k] == next_bottom_val:
                best_next = max(best_next, dp_next[downs[k]])
        
        dp_cur[j] = cur_score + best_next
    
    # 한 단계 올라가기( i -> i-1 ): dp_next <- dp_cur
    dp_next, dp_cur = dp_cur, dp_next

# 이제 dp_next 중 최댓값이 정답에 해당
ans = max(dp_next)
print(ans)