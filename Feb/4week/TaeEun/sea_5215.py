from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(1, N+1):
        for comb in combinations(ingredients, i):
            sum_of_scores = 0
            sum_of_calories = 0
            for score, calorie in comb:
                sum_of_scores += score
                sum_of_calories += calorie
            if sum_of_calories > L:
                continue
            ans = max(ans, sum_of_scores)

    print(f'#{tc} {ans}')