# 입력 변수
# 전역: T
# 테케 당: N, L, ingredients, max_score


# 로직
# 1 테케당 입력
# 	ㄱ. N, L, ingredients
# 	ㄴ. [list 컴프리핸션으로 재료에 대한 T, K 받기 for _ in range N] 
#	ㄷ. 리스트에 dfs(백트래킹) 돌아서 종료조건
#       1. dfs로 cal가 > L을 초과할 때 탐색 종료
#       2. 모든 재료를 확인했을 때 탐색 종료

def dfs(idx, score, cal):
    global max_score

    # 칼로리가 제한 `L`을 초과하면 탐색 중단
    if cal > L:
        return

    # 현재까지의 점수 갱신
    max_score = max(max_score, score)

    # 모든 재료를 확인한 경우 탐색 종료
    if idx == N:
        return

    # 현재 재료를 선택하는 경우
    dfs(idx + 1, score + ingredients[idx][0], cal + ingredients[idx][1])

    # 현재 재료를 선택하지 않는 경우
    dfs(idx + 1, score, cal)


T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    
    max_score = 0
    dfs(0, 0, 0)

    print(f"#{tc} {max_score}")