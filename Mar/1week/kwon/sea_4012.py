# 요리사 

# 1. 두 그룹으로 나누는 조합 찾기
# 2. A가 정해지면 B는 자동으로 정해짐
#    B = ingre - A
# 3. 시너지 계산 
#    ㄴ A 그룹에서 두 개씩 뽑아 시너지 계산
#    ㄴ B 그룹에서 두 개씩 뽑아 시너지 계산 
# 4. 최솟값 갱신 

from itertools import combinations

def calculate_synergy(ingredients, S):
    synergy = 0 # 함수 실행될 때마다 시너지 값 초기화
    for i in range(len(ingredients)):
        for j in range(i+1, len(ingredients)): # i 다음 idx 부터 뽑아야하므로 i+1
            synergy += S[ingredients[i]][ingredients[j]] + S[ingredients[j]][ingredients[i]]
            # 대칭이므로 [i][j] + [j][i]
    return synergy

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 재료 개수
    ingre = [i for i in range(N)] # 재료 리스트
    S = [list(map(int, input().split())) for _ in range(N)]
    min_value = float('inf') # 최솟값 설정

    for A in combinations(ingre, N//2): # 2가지 요리할 수 있는 재료 조합 찾기
        A = list(A)
        B = [i for i in range(N) if i not in A]

        synergy_A = calculate_synergy(A, S)
        synergy_B = calculate_synergy(B, S)

        min_value = min(min_value, abs(synergy_A - synergy_B))

    print(f'#{tc} {min_value}')



        




    