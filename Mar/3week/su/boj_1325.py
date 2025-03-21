from collections import defaultdict
from collections import deque

N, M = map(int, input().split())
graph = defaultdict(list)


for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

answer = 0
answer_li = []  

def bfs(start):
    queue = deque()
    queue.append((start, 1))
    visited[start] = 1
    count = 0

    while queue:
        node, depth = queue.popleft()
        count += 1

        for next_node in graph[node]:
            if visited[next_node]:
                continue
            queue.append((next_node, depth + 1))
            visited[next_node] = 1

    return count

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    hacked = bfs(i)
    
    if hacked > answer:
        answer_li = [i]
        answer = hacked
    elif hacked == answer:
        answer_li.append(i)

print(*answer_li)