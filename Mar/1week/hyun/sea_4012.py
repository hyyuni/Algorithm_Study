# DFS 백트래킹을 활용해 식재료의 인덱스에 대한 조합을 구하고 최소값 갱신하기
def dfs(step, lst1, lst2):
    global min_v   
    if step == N:
        if len(lst1) == N // 2 and len(lst2) == N // 2:
            sum1, sum2 = 0, 0
            
            # 각 그룹(lst1, lst2)의 모든 재료 조합을 순회하며 맛 점수 합산
            for i in range(N // 2):
                for j in range(N // 2):
                    # arr[i][j]는 i번과 j번 식재료가 함께 요리될 때의 시너지 효과
                    sum1 += arr[lst1[i]][lst1[j]]  # 첫 번째 요리의 총 맛 점수 계산
                    sum2 += arr[lst2[i]][lst2[j]]  # 두 번째 요리의 총 맛 점수 계산
            
            # 두 요리의 맛 점수 차이의 절댓값을 구하고 최소값을 갱신
            min_v = min(min_v, abs(sum1 - sum2))
        return
    
    # 첫 번째 요리 그룹(lst1)의 크기가 N//2보다 작을 경우
    # 현재 step(식재료의 인덱스)을 lst1에 추가하고 DFS 탐색을 이어간다.
    if len(lst1) < N // 2:
        dfs(step + 1, lst1 + [step], lst2)
    
    # 두 번째 요리 그룹(lst2)의 크기가 N//2보다 작을 경우
    # 현재 step(식재료의 인덱스)을 lst2에 추가하고 DFS 탐색을 이어간다.
    if len(lst2) < N // 2:
        dfs(step + 1, lst1, lst2 + [step])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = float('inf')  # 최소값 초기화
    
    dfs(0, [], [])  # DFS 탐색
    print(f'#{tc} {min_v}')