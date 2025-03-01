# 풍선팡 보너스 게임

def calculate_score(x, y):
    sum_row = sum(numbers[x])
    sum_column = sum(numbers[j][y] for j in range(n))
    score = sum_row + sum_column - numbers[x][y] # 중복값 처리
    return score

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    numbers = [list(map(int, input().split())) for _ in range(n)]
    max_score = 0

    for i1 in range(n):
        for j1 in range(n):
            score1 = calculate_score(i1, j1)
            for i2 in range(n):
                for j2 in range(n):
                    if i1 == i2 and j1==j2:
                        continue
                    score2 = calculate_score(i2, j2)
                    max_score = max(max_score, abs(score1-score2))

    print(f'#{tc} {max_score}')