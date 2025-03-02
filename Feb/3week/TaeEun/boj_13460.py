from collections import deque
from copy import deepcopy
from pprint import pprint


N, M= map(int, input().split())
board = [list(input()) for _ in range(N)]

directions = [(1,0), (0,1), (0,-1), (-1,0)]

for i in range(N):
    for j in range(M):
        value = a[i][j]
        if value == 'R':
            red_coord = [i,j]
            board[i][j] = '.'
        elif value == 'B':
            blue_coord = [i,j]
            board[i][j] = '.'
        elif value == 'O':
            hole_coord = [i,j]



def beads_bfs(red, blue):
    global board
    q = deque()
    visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)] # 4차원으로 구성해야 rr rc이 같아도 br bc가 다르면 다른 상태
    q.append([red, blue, 0])
    rr, rc = red
    br, bc = blue
    visited[rr][rc][br][bc] = 1

    while q:
        l = len(q)
        for _ in range(l):
            r, b, turn = q.popleft()
            if turn > 10:
                return -1
            for dr, dc in directions:
                cur_rr, cur_rc = r
                cur_br, cur_bc = b

                priority = 0
                if dr == 1 and cur_br > cur_rr:
                    priority = 1                   
                elif dc == 1 and cur_bc > cur_rc:
                    priority = 1
                elif dr == -1 and cur_br < cur_rr:
                    priority = 1
                elif dc == -1 and cur_bc < cur_rc:
                    priority = 1
                
                
                if priority == 0: #red 먼저
                    board[cur_rr][cur_rc] = '.'
                    red_meet_O = False
                    while True:
                        new_rr, new_rc = cur_rr+dr, cur_rc+dc
                        
                        if board[new_rr][new_rc] == '.':
                            cur_rr, cur_rc = new_rr, new_rc
                            continue
                        elif board[new_rr][new_rc] == 'O':
                            red_meet_O = True
                            break
                        break
                    
                    if not red_meet_O:
                        board[cur_rr][cur_rc] = 'R'
                    

                    board[cur_br][cur_bc] = '.'
                    blue_meet_O = False

                    while True:
                        new_br, new_bc = cur_br+dr, cur_bc+dc
                        
                        if board[new_br][new_bc] == '.':
                            cur_br, cur_bc = new_br, new_bc
                            continue
                        elif board[new_br][new_bc] == 'O':
                            blue_meet_O = True
                            break
                        break
                    board[cur_br][cur_bc] = 'B'
                    if blue_meet_O:
                        continue

                    if red_meet_O:
                        return turn + 1

                    if visited[cur_rr][cur_rc][cur_br][cur_bc]:
                        continue

                    
                    q.append([[cur_rr, cur_rc], [cur_br, cur_bc], turn+1, board])
                    visited[cur_rr][cur_rc][cur_br][cur_bc] = 1
                    
                
                elif priority == 1: #blue 먼저

                    board[cur_br][cur_bc] = '.'
                    blue_meet_O = False

                    while True:
                        
                        new_br, new_bc = cur_br+dr, cur_bc+dc
                        if board[new_br][new_bc] == '.':
                            cur_br, cur_bc = new_br, new_bc
                            continue
                        elif board[new_br][new_bc] == 'O':
                            blue_meet_O = True
                            break
                        break
                    
                    if blue_meet_O:
                        continue
                    
                    board[cur_br][cur_bc] = 'B'

                    board[cur_rr][cur_rc] = '.'

                    while True:
                        new_rr, new_rc = cur_rr+dr, cur_rc+dc
                        if board[new_rr][new_rc] == '.':
                            cur_rr, cur_rc = new_rr, new_rc
                            continue
                        elif board[new_rr][new_rc] == 'O':
                            return turn + 1
                        break
                    board[cur_rr][cur_rc] = 'R'

                    if visited[cur_rr][cur_rc][cur_br][cur_bc]:
                        continue

                    q.append([[cur_rr, cur_rc], [cur_br, cur_bc], turn+1, board])
                    visited[cur_rr][cur_rc][cur_br][cur_bc] = 1
    return -1

print(beads_bfs(red_coord, blue_coord))




''' gpt 정답
from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

red_r = red_c = blue_r = blue_c = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red_r, red_c = i, j
            board[i][j] = '.'  # 보드에서 구슬 빼기
        elif board[i][j] == 'B':
            blue_r, blue_c = i, j
            board[i][j] = '.'  # 보드에서 구슬 빼기
        # 구멍 'O'은 그대로 둠

# 상하좌우 정의
directions = [(-1,0),(1,0),(0,-1),(0,1)]

# 방문 배열: visited[red_r][red_c][blue_r][blue_c]
visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
visited[red_r][red_c][blue_r][blue_c] = True

def move_until_stop(r, c, dr, dc):
    """(r, c)에서 (dr, dc) 방향으로 벽(#) 또는 구멍(O)을 만날 때까지 굴린다.
       - 최종 위치 (nr, nc),
       - 구멍에 빠졌는지 여부(hole),
       - 몇 칸 이동했는지(move_count)를 반환
    """
    move_count = 0
    while True:
        nr = r + dr
        nc = c + dc
        # 벽(#)이면 끝
        if board[nr][nc] == '#':
            return (r, c, False, move_count)
        # 구멍(O)이면 빠짐
        if board[nr][nc] == 'O':
            return (nr, nc, True, move_count + 1)
        # 빈 칸(.)이면 계속 이동
        r, c = nr, nc
        move_count += 1

q = deque()
q.append((red_r, red_c, blue_r, blue_c, 0))  # (빨강r, 빨강c, 파랑r, 파랑c, 이동 횟수)

while q:
    rr, rc, br, bc, depth = q.popleft()
    
    # 이미 10번을 사용했다면, 더 이상 진행 불가능 (10 이하로만)
    if depth >= 10:
        break
    
    for dr, dc in directions:
        # 빨강 구슬 이동
        nr_r, nr_c, red_in_hole, r_dist = move_until_stop(rr, rc, dr, dc)
        # 파랑 구슬 이동
        nb_r, nb_c, blue_in_hole, b_dist = move_until_stop(br, bc, dr, dc)
        
        # 파랑 구슬이 구멍에 빠지면 실패이므로 무시
        if blue_in_hole:
            continue
        
        # 빨간 구슬만 구멍에 빠지면 성공
        if red_in_hole and not blue_in_hole:
            print(depth + 1)
            exit()
        
        # 둘 다 구멍이 아닌데 최종 위치가 겹친다면, 더 많이 이동한 공을 한 칸 뒤로
        if nr_r == nb_r and nr_c == nb_c:
            # 거리가 더 큰 쪽(=더 뒤늦게 도착한 공)을 한 칸 뒤로
            if r_dist > b_dist:
                nr_r -= dr
                nr_c -= dc
            else:
                nb_r -= dr
                nb_c -= dc
        
        # 방문한 적 없으면 큐에 삽입
        if not visited[nr_r][nr_c][nb_r][nb_c]:
            visited[nr_r][nr_c][nb_r][nb_c] = True
            q.append((nr_r, nr_c, nb_r, nb_c, depth + 1))

# 여기까지 도달하면 10번 이하로는 성공 못 했다는 뜻
print(-1)


'''