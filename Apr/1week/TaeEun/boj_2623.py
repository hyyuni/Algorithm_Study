from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
in_degree = [0]*(N+1)

for _ in range(M):
    data = list(map(int, input().split()))
    k = data[0]
    sequence = data[1:]
    for i in range(k-1):
        adj[sequence[i]].append(sequence[i+1])
        in_degree[sequence[i+1]] += 1

queue = deque()
for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)

result = []
while queue:
    now = queue.popleft()
    result.append(now)
    for nxt in adj[now]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            queue.append(nxt)

if len(result) == N:
    for x in result:
        print(x)
else:
    print(0)
