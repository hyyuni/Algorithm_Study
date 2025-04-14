# 2. 조합으로 풀기

from itertools import combinations

def cal(team):
    cnt = 0
    for x, y in combinations(team, 2):
        cnt += arr[x][y] + arr[y][x]
    return cnt

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = float('inf')
players = [i for i in range(N)]

for start in combinations(players, N//2):
    link = list(set(players) - set(start))

    abil_1 = cal(start)
    abil_2 = cal(link)

    res = abs(abil_1 - abil_2)
    min_v = min(min_v, res)

    # 최솟값이 0이 됐을 때, 더 작은 값은 존재 X
    if min_v == 0:
        break

print(min_v)

# 1. dfs 백트래킹으로 풀기

def cal(start, link):
    abil_1 = 0
    abil_2 = 0
    for i in range(N//2):
        for j in range(N//2):
            abil_1 += arr[start[i]][start[j]]
            abil_2 += arr[link[i]][link[j]]
    return abs(abil_1 - abil_2)

def dfs(cnt, start, link):
    global min_v
    # Pruning
    # 1. 최솟값 0이 됐을 때, 더 확인할 필요 없음
    if min_v == 0:
        return
    # 2. 한 팀이 이미 M명을 초과해 버렸을 경우 함수 종료해도 됨
    if len(start)>N//2 or len(link)>N//2:
        return

    if cnt == N:
        if len(start) == len(link):
            min_v = min(min_v, cal(start, link))
        return
    
    dfs(cnt+1, start+[cnt], link) # start팀을 선택했을 때
    dfs(cnt+1, start, link+[cnt]) # link팀을 선택했을 때


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_v = float('inf')

dfs(0, [], [])

print(min_v)