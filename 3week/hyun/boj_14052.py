import copy

def dfs(*lst):
    cnt = 0
    # dfs를 계속 수행할 arr 복사본 만들기
    temp = copy.deepcopy(arr)
    # 방문 처리할 리스트 생성
    visited = [[0]*M for _ in range(N)]
    # 안전 구역에 벽 채우기
    for i, j in lst:
        temp[i][j] = 1
    
    # virus를 퍼뜨릴 실행할 함수 만들기
    def virus(si, sj):
        visited[si][sj] = 1

        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = si + di, sj + dj
            if 0<= ni < N and 0<= nj <M and visited[ni][nj] == 0 and temp[ni][nj] == 0:
                temp[ni][nj] = 2
                virus(ni, nj)

    # 벽을 세운 후 virus 퍼뜨리기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2 and visited[i][j] == 0:
                virus(i,j)

    # 안전 구역 카운트하기
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                cnt += 1
    
    return cnt

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_v = 0
# 리스트 생성
wall = []

# wall 리스트 조합 채우기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            # 튜플 형태로 arr의 i, j값 넣어주기 
            wall.append((i,j))

# 러시아 국기 풀듯이 3가지 조합에 대한 범위 만들기
for i in range(len(wall)-2):
    for j in range(i+1, len(wall)-1):
        for k in range(j+1, len(wall)):
            max_v = max(max_v, dfs(wall[i], wall[j], wall[k]))

print(max_v)