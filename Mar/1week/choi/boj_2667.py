def dfs(i, j):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    arr[i][j] = '0'
    for dir in range(4):
        if  0 <= i+dx[dir] < N and 0 <= j+dy[dir] < N:
            if arr[i+dx[dir]][j+dy[dir]] != '0':
                cnt += 1
                ni = i+dx[dir]
                nj = j+dy[dir]
                arr[ni][nj] = '0'
                dfs(ni, nj)
    return cnt

N  = int(input())
arr = [list(map(str, input())) for _ in range(N)]
big_house = 0
house_cnt = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != '0':
            cnt = 1
            dfs(i, j)
            big_house += 1
            house_cnt.append(cnt)
print(big_house)
ans = sorted(house_cnt)
for res in ans:
    print(res)