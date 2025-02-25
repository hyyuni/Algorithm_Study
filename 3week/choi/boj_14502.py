from copy import deepcopy
N ,M = map(int, input().split())
lab = [list(map(int, input().split()))for i in range(N)]

wall_idx = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            wall_idx.append((i,j))

max_safe = 0    

def wall3(count, start):
    global max_safe
    if count == 3:
        max_safe = max(max_safe, virus())
        return

    for i in range(start, len(wall_idx)):
        x, y = wall_idx[i]
        lab[x][y] = 1
        wall3(count+1, i+1)
        lab[x][y] = 0

def virus():
    jjap_lab = deepcopy(lab)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # for i in range(N):
    #     for j in range(M):
    #         if jjap_lab[i][j] == 2:
    #             for k in range(4):
    #                 ni, nj = i + di[k], j + dj[k]
    #                 if 0 <= ni < N and 0 <= nj < M and jjap_lab[ni][nj] == 0 and visited[ni][nj] == 0:
    #                     jjap_lab[ni][nj] = 2
    #                     visited[ni][nj] = 1
    def virus_dfs(i, j):
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and jjap_lab[ni][nj] == 0:
                jjap_lab[ni][nj] = 2
                virus_dfs(ni, nj)
    
    for i in range(N):
        for j in range(M):
            if jjap_lab[i][j] == 2:
                virus_dfs(i, j)

    safe = 0
    for i in range(N):
        for j in range(M):
            if jjap_lab[i][j] == 0:
                safe += 1
    return safe
    
wall3(0, 0)
print(max_safe)