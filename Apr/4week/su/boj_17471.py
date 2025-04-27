from collections import defaultdict
from itertools import combinations

N = int(input())
INF = int(1e9)
person_list = [INF * -1] + list(map(int, input().split()))
info = defaultdict(list)
cnt_info = defaultdict(int)

for i in range(1, N+1):
    line = list(map(int, input().split()))
    area_cnt, linked = line[0], line[1:]
    cnt_info[i] = area_cnt
    info[i] = linked

def dfs(cur_node):
    global visited, target_area, connected_result, cnt

    if connected_result:
        return

    # 방문체크를 한다.
    if cnt == len(target_area):
        connected_result = True
        return
    
    for next_node in info[cur_node]:
        if next_node not in target_area:
            continue
        if visited[next_node]:
            continue

        visited[next_node] = True
        cnt += 1
        dfs(next_node)

def is_connected(area):  # dfs
    global target_area, visited, connected_result, cnt
    cnt = 0
    connected_result = False
    target_area = area
    visited = [False] * (N + 1)    

    visited[target_area[0]] = True
    cnt += 1
    
    dfs(target_area[0])  # area[0]에서 출발해서 연결된 모든 지점을 dfs로 방문한다.
    if connected_result:
        return True
    return False

cnt = 0
target_area = []
visited = []
connected_result = False

area_li = [i for i in range(1, N + 1)]
total_p = sum(person_list[1:])
answer = INF

for i in range(1, (N // 2) + 1):
    for area_1 in combinations(area_li, i):
        
        p_1 = 0
        for a in area_1:
            p_1 += person_list[a]

        p_2 = total_p - p_1
        gap = abs(p_1 - p_2)
        if gap < answer:  # 인구 차이 최솟값을 갱신할 가능성이 있을 때만 dfs 시작하기. 
            area_2 = set(area_li) - set(area_1)  # 차집합
            if is_connected(list(area_1)) and is_connected(list(area_2)):
                answer = gap  # 인구 차이의 최솟값 갱신
            

print(answer if answer != INF else -1) 