def dfs(cnt,prob):
    global max_v
    if prob <= max_v:
        return
    if prob == 0:
        return 
    if cnt == N:
        print(a)
        max_v = max(max_v,prob)
        print(max_v)
        return
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            a.append(work[cnt][j])
            dfs(cnt+1,prob*(work[cnt][j]/100))
            a.pop()
            visited[j] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    work = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    a = []
    max_v = 0
    dfs(0,100.0)
    print(f'#{tc} {max_v:.6f}')

# def dfs(cnt, prob):
#     global max_v

#     if prob <= max_v:  # 가지치기 1: 현재 확률이 이미 최댓값보다 낮다면 중단
#         return
#     if prob == 0:  # 가지치기 2: 확률이 0이 되는 경우 중단
#         return
#     if max_v == 100.0:  # 가지치기 3: 최대 확률 도달 시 중단
#         return

#     # 가지치기 4: 앞으로 남은 최댓값을 곱해도 max_v보다 작다면 중단
#     remaining_max = 1
#     for k in range(cnt, N):
#         remaining_max *= max(work[k]) / 100  # 남은 행에서 최댓값 사용
#     if prob * remaining_max <= max_v:
#         return

#     if cnt == N:
#         max_v = max(max_v, prob)
#         return

#     for j in range(N):
#         if not visited[j]:  # 해당 열이 아직 선택되지 않았다면 진행
#             visited[j] = True
#             dfs(cnt + 1, prob * (work[cnt][j] / 100))  # 확률 변환
#             visited[j] = False  # 백트래킹


# # 입력 처리
# T = int(input())  # 테스트 케이스 개수
# for test_case in range(1, T + 1):
#     N = int(int())  # N명의 직원, N개의 작업
#     work = [list(map(int, input().split())) for _ in range(N)]  # 성공 확률 테이블

#     max_v = 0  # 최대 확률 값
#     visited = [False] * N  # 방문한 열(작업) 체크

#     dfs(0, 1.0)  # DFS 탐색 시작

#     # 출력 (퍼센트 단위로 소수점 6자리까지 반올림)
#     print(f"#{test_case} {max_v * 100:.6f}")