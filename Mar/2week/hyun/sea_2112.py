from itertools import product
from copy import deepcopy

# 성능검사 함수: 필름이 성능 검사를 통과하는지 체크
def checklist(graph):
    # K가 1이면 무조건 통과 (한 칸만 있어도 조건 만족)
    if K == 1:
        return True
    
    # 각 열마다 검사 진행
    for col in range(W):
        cnt = 1  # 연속된 셀의 개수를 세는 변수
        
        for row in range(D - 1):
            # 같은 특성이 연속되면 cnt 증가
            if graph[row][col] == graph[row + 1][col]:
                cnt += 1
                if cnt >= K:
                    break  # 조건 만족하면 이 열은 더 이상 검사할 필요 없음
            else:
                cnt = 1  # 특성이 바뀌면 다시 초기화
        
        else:  # for-else문: 중간에 break 없이 끝까지 갔다면 조건 불만족
            return False
    
    return True  # 모든 열이 조건을 만족하면 True 반환

# 약품 투입 함수: 특정 행들(lst)을 선택한 약품(types)으로 변경
def injection(graph_t, lst, types):
    for row_idx, drug_type in zip(lst, types):
        graph_t[row_idx] = [drug_type] * W

# DFS 함수: 약품을 투입할 행을 선택하는 모든 경우를 탐색
def dfs(idx, drug_cnt, selected_rows):
    global ans, find
    
    # 약품을 투입할 행이 drug_cnt개 만큼 선택되었으면 실제로 투입해보기
    if len(selected_rows) == drug_cnt:
        for drug_types in product((0, 1), repeat=drug_cnt):
            injection(graph, selected_rows, drug_types)  # 약품 투입
            
            if checklist(graph):  # 성능검사 통과 여부 체크
                ans = min(ans, drug_cnt)
                find = True
                return
            
            # 원상복구 (백트래킹)
            for row in selected_rows:
                graph[row] = backup[row]
        return
    
    # 종료조건: 모든 행 탐색 완료 or 이미 최소값 발견 시 종료
    if idx == D or find:
        return
    
    # 현재 idx 행을 선택하는 경우와 선택하지 않는 경우로 나누어 탐색 진행 (DFS)
    dfs(idx + 1, drug_cnt, selected_rows + [idx])  # 선택 O
    dfs(idx + 1, drug_cnt, selected_rows)          # 선택 X

# 메인 실행부
T = int(input())

for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    
    graph = [list(map(int, input().split())) for _ in range(D)]
    backup = deepcopy(graph)  # 원본 그래프를 백업 (복구용)
    
    ans = K       # 초기값 설정 (최악의 경우 약품을 K번 투입해야 함)
    find = False  # 정답 발견 여부 플래그
    
    # 최초 상태에서 이미 성능검사를 통과한다면 약품 투입 필요 없음 (0 출력)
    if checklist(graph):
        print(f'#{tc}', 0)
    
    else:
        # 약품 투입 횟수를 최소화하기 위해 적은 횟수부터 증가시키며 탐색 진행
        for drug_cnt in range(1, D + 1):
            dfs(0, drug_cnt, [])
            
            if find:  # 최소 횟수 발견 시 더 이상 탐색하지 않고 종료
                break
        
        print(f'#{tc}', ans)