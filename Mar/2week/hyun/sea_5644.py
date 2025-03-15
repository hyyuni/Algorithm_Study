from collections import deque

# x, 상, 우, 하, 좌
directions = [(0,0), (-1,0), (0,1), (1,0), (0,-1)]

T = int(input())

def bfs(sy, sx, cnt):
    q = deque([(sy, sx, 0)])
    v = [[0] * 10 for _ in range(10)]
    v[sy][sx] = 1
    
    while q:
        for _ in range(len(q)):
            cy, cx, step = q.popleft()
            if step == cnt:
                continue
            for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < 10 and 0 <= nx < 10 and not v[ny][nx]:
                    v[ny][nx] = 1
                    q.append((ny, nx, step + 1))
    
    return v

def charge(A_move, B_move, bc_info):
    bc_maps = [[[[] for _ in range(10)] for _ in range(10)] for _ in range(len(bc_info))]
    # 각 bc_id 마다 충전 계산을 위해 '3차원 리스트'로 생성하기 [z][y][x]
    
    for bc_id, (sx, sy, cnt, _) in enumerate(bc_info): # bc_info 리스트에서 정보 뽑기
        # 주의! 디버깅한 부분 sx와 sy좌표를 반대로 가져와야 우리가 생각하는 대로 들어감!!
        bc_range = bfs(sy-1, sx-1, cnt) # bfs를 돌아 각 충전소 범위 구하기
        for y in range(10):
            for x in range(10):
                if bc_range[y][x]: # 만약 해당 위치가 충전 범위 내라면
                    bc_maps[bc_id][y][x].append(bc_id)
    
    ax, ay, bx, by = 0, 0, 9, 9 # A는(0,0)부터 B는 (9,9) 부터 시작
    total_charge = 0
    
    for m in range(len(A_move)): # 여기서도 x와 y 순서 주의해야함..
        ax, ay = ax + directions[A_move[m]][1], ay + directions[A_move[m]][0]
        bx, by = bx + directions[B_move[m]][1], by + directions[B_move[m]][0]
        
        A_bc, B_bc = set(), set()
        for bc_id in range(len(bc_info)):
            if bc_maps[bc_id][ay][ax]:
                A_bc.add(bc_id)
            if bc_maps[bc_id][by][bx]:
                B_bc.add(bc_id)
        
        max_v = 0
        for a in A_bc or [-1]:
            for b in B_bc or [-1]:
                charge = 0
                if a == b and a != -1:
                    charge = bc_info[a][3]
                else:
                    if a != -1:
                        charge += bc_info[a][3]
                    if b != -1:
                        charge += bc_info[b][3]
                max_v = max(max_v, charge)
        
        total_charge += max_v
    
    return total_charge

for tc in range(1, T+1):
    M, A = map(int, input().split())
    A_moves = list(map(int, input().split()))
    B_moves = list(map(int, input().split()))
    bc_info = [list(map(int, input().split())) for _ in range(A)]
    
    A_moves.insert(0, 0) # 0번 idx에 0 추가하는 메서드, 초기 위치에서 충전량을 고려해야 함
    B_moves.insert(0, 0)
    
    ans = charge(A_moves, B_moves, bc_info)
    print(f"#{tc} {ans}")