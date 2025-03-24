import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations

def attack(archers, enemies):
    killed_enemies = set()

    for archer in archers:
        ay, ax = archer
        min_dist = float('inf')
        target = None # target을 업데이트하기 위한 None값

        for ey, ex in enemies:
            dist = abs(ay-ey) + abs(ax-ex)
            if dist > D: # dist가 사정거리 초과하면 안 됨
                continue
            if dist < min_dist or (dist == min_dist and (target is None or ex < target[1])):
                # 가장 가까운 적이 여럿일 때, target은 가장 왼쪽 적이라고 했으므로 ex가 가장 작은 적을 target 해야 한다 target[1] = x좌표
                min_dist = dist
                target = (ey,ex)

        if target: # 타겟된 적들을 제거한 적 set에 추가
            killed_enemies.add(target)

    return killed_enemies
            
def move(enemies):
    move_enemies = set()
    
    for ey, ex in enemies:
        if ey+1 < N: # 아직 적이 성에 도착하지 못했다면,
            move_enemies.add((ey+1, ex)) # 아래로 1칸씩 이동하기
    
    return move_enemies

N, M, D = map(int, input().split())

# 궁수 배치할 성벽을 -1값으로 맨 아래 패딩하기
graph = [list(map(int, input().split())) for _ in range(N)] + [[-1]*M] 
enemies = set()
arrow = set()
max_kill = 0

# enemy와 arrow 좌표 값 추가하기
for y in range(N+1):
    for x in range(M):
        if graph[y][x] == 1:
            enemies.add((y,x))
        if graph[y][x] == -1:
            arrow.add((y,x))

# 궁수를 배치할 수 있는 조합 구하기
comb_arrow = list(combinations(arrow, 3))

for archers in comb_arrow:
    cur_enemies = enemies.copy()
    total_kill = 0

    while cur_enemies: # 적들이 살아있는 동안,
        # 궁수들이 제거할 적 선택
        killed_enemies = attack(archers, cur_enemies)
        total_kill += len(killed_enemies)
        cur_enemies -= killed_enemies

        # 궁수의 공격이 끝나면 적 이동
        cur_enemies =  move(cur_enemies)

    max_kill = max(max_kill, total_kill)

print(max_kill)