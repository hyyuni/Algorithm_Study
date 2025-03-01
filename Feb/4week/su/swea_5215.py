T = int(input())

for test_case in range(1, T+1):
    N, L = map(int, input().split())
    food = []

    for i in range(N):
        T, K = map(int, input().split())
        food.append((T, K))
        
    answer = 0 # 맛 점수
    
    def dfs(start_idx, temp_calorie, temp_taste):
        global answer

        for i in range(start_idx, N):
            t, k = food[i]
            calorie = temp_calorie + k
            taste = temp_taste + t

            if calorie > L: # 더 이상 볼 필요 없음
                continue
                # return # 주의: return으로 할 시 다음 조합 해보지도 못하고 종료됨
            if taste > answer: # 최댓값 갱신
                answer = taste
            
            dfs(i+1, calorie, taste)

    
    dfs(0, 0, 0)

    print(f"#{test_case} {answer}")