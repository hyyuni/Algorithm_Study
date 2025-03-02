def dfs(s):
    ans_dfs.append(s) # 방문한 노드를 결과 리스트에 추가
    visited[s] = 1 # 방문 표시

    for n in adj[s]: # 현재 노드와 인접한 모든 노드 순회
        if not visited[n]: # 아직 노드에 방문한 상태가 아니면
            dfs(n) # 재귀 탐색

def bfs(s):
    queue = [] # queue 선언
    queue.append(s) # queue에 시작 노드 추가
    ans_bfs.append(s) # 결과 리스트에 추가
    visited[s] = 1 # 방문 = 1, 미방문 = 0

    while queue: # queue가 빌 때까지
        c = queue.pop(0) # 큐의 앞에서 하나 꺼내기
        for n in adj[c]: # 현재 노드와 인접한 모든 노드를 탐색
            if not visited[n]: # 아직 노드에 방문한 상태가 아니면
                queue.append(n)
                ans_bfs.append(n)
                visited[n] = 1


N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)] # 인접 리스트 생성하기
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e) # 양방향 그래프를 저장 ex.1->2 2->1
    adj[e].append(s)

# 오름차순 정렬
for i in range(1, N+1): # 정점 번호가 작은 것부터 방문
    adj[i].sort()

visited = [0]*(N+1) # 방문 리스트 초기화
ans_dfs = []
dfs(V)

visited = [0]*(N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)