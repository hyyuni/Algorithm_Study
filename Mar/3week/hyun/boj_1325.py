from collections import deque

def bfs(n):
    v = [0] * (N+1)
    q = deque([n])
    v[n] = 1
    cnt = 0

    while q:
        cur_pos = q.popleft()
        cnt += 1 

        for next_pos in adj[cur_pos]:
            if not v[next_pos]:
                v[next_pos] = 1 
                q.append(next_pos)

    return cnt

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
lst = [0]
ans = []
for _ in range(M):
    s, e = map(int, input().split())
    adj[e].append(s)

for i in range(1, N+1):
    res = bfs(i)
    lst.append(res)

max_v = max(lst)

for i in range(N+1):
    if lst[i] == max_v:
        ans.append(i)

print(*ans)