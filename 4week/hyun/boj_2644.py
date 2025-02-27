from collections import deque

def bfs(s, e):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        cur_pos = q.popleft()
        if cur_pos == e:
            return visited[e] - 1 # 나와 한 칸 떨어진 노드라면 1촌이므로
        for n in chon_lst[cur_pos]:
            if visited[n] == 0:
                q.append(n)
                visited[n] = visited[cur_pos] + 1 # 연결된 노드를 방문할 때 1촌씩 더해주기
    return -1



n = int(input())
man1, man2 = map(int, input().split())
m = int(input())

visited = [0] * (n+1)
chon_lst = [[] for _ in range(n+1)] # 인덱싱 1부터 사용할 예정이므로

for _ in range(m):
    x, y = map(int, input().split())
    chon_lst[x].append(y)
    chon_lst[y].append(x)

res = bfs(man1, man2)

print(res)