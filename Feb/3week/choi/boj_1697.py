from collections import deque

def bfs(n, k):
    MAX = 100000
    visited = [-1] * (MAX + 1)
    queue = deque([n])
    visited[n] = 0 

    while queue:
        x = queue.popleft()

        if x == k: 
            return visited[x]
        for next_x in (x - 1, x + 1, x * 2):
            if 0 <= next_x <= MAX and visited[next_x] == -1:
                visited[next_x] = visited[x] + 1
                queue.append(next_x)

N, K = map(int, input().split())
print(bfs(N, K))
