# 작업순서

# 위상 정렬
# 그래프
# - 유향
# - 순환 X
# 유향에 순환하지 않는 그래프 : DAG
# 이걸 순회하기 위한 방법 : 위상 정렬
# 5의 선수 진도 -> 1, 8
# 1,8을 확인 할 필요 X, 갯수로 파악
# 바로 이전 것만 확인하면 됨(중복체크 하지 않아도 됨)
# 1 : 1개 2: 1개 3: 1개 4 : 0개 5 : 2개 6 : 2개 7 : 1개 8: 0개 9 : 1개
# 시작점 : 0인 것부터 시작. queue 이용
# 4, 8, 1, 9, 2, 5, 3, 7, 6
# 4 가 pop 되면서 1의 값 줄여줌 (1: 1개 -> 0개)
# 1은 작업 시작 가능한 상태가 됨
# 큐에서 빠지는 순서대로 작업 시작

from collections import deque

T = 10

def bfs():
    result = []
    q = deque()

    for i in range(1, v+1):
        if num[i] == 0: # 진입차수가 0
            q.append(i)

    while q:
        c = q.popleft()
        result.append(c)

        for j in graph[c]:
            num[j] -= 1
            if num[j] == 0:
                q.append(j)
    print(*result)

for tc in range(1, T + 1):
    v, e = map(int, input().split())
    numbers = list(map(int, input().split()))
    num = [0] * (v+1) # 진입차수 체크
    graph = [[] for _ in range(v+1)]


    for i in range(0, e * 2, 2):
        start, end = numbers[i], numbers[i + 1]
        graph[start].append(end)

    for i in range(1, v+1):
        for j in graph[i]:
            num[j] += 1

    print(f'#{tc} ', end = '')
    bfs()