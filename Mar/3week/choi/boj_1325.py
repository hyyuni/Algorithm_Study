from collections import deque
 
N, M = map(int, input().split())
computer = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    computer[B].append(A)
   
 ``
def bfs(start):
    q = deque()
    q.append(start)
    cnt = 0
 
    visited = [0] * (N + 1)
    visited[start] = 1

    while q:
        now = q.popleft()
        for daum in computer[now]:
            if not visited[daum]:
                visited[daum] = 1
                q.append(daum)
                cnt += 1
    return cnt
 
result = [0]
for start in range(1, len(computer)):
    a = bfs(start)
    result.append(a)
max_v = max(result)
ans = []
for i in range(1, N+1):
    if result[i] == max_v:
        ans.append(i)
print(*ans)