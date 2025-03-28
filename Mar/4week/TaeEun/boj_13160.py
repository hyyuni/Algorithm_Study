
import heapq

N = int(input())
edges = []

h = []

for i in range(N):
    s, e = map(int, input().split())
    edges.append((s, e))
    # 시작과 끝을 0과 1로 표현
    # 좌표가 같을 때 시작 이벤트가 먼저 나오게
    heapq.heappush(h, (s, 0, i+1))  # i+1은 1based로 변경
    heapq.heappush(h, (e, 1, i+1))

count = 0      # 현재 겹치는 구간 수
max_count = 0  # 클리크 크기 최대
best_coord = 0 # 최대 겹침이 발생한 좌표

# 힙에서 이벤트를 하나씩 꺼내며 선 스위핑
while h:
    coord, s_or_e, idx = heapq.heappop(h)
    
    if s_or_e == 0:
        # 시작 이벤트
        count += 1
        if count > max_count:
            max_count = count
            best_coord = coord
    else:
        # 끝 이벤트
        count -= 1

# best_coord를 포함하는 구간, 즉 최대 클리크를 찾기
clique = []
for i, (s, e) in enumerate(edges, start=1):
    if s <= best_coord <= e:
        clique.append(i)

clique.sort()

# 결과 출력
print(max_count)
print(*clique)
