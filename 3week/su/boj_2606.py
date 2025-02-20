# https://www.acmicpc.net/problem/2606
import sys
from collections import defaultdict
from collections import deque

N = int(input())
M = int(input())

cnt = 0
graph = defaultdict(list)
visited = defaultdict(bool)

for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)
visited[1] = True

while queue:
    cur_node = queue.popleft()
    for next_node in graph[cur_node]:
        if visited[next_node]:
            continue
        queue.append(next_node)
        visited[next_node] = True
        cnt += 1
print(cnt)