# def dfs():

N = int(input())
meeting = [list(map(int,input().split())) for _ in range(N)]
meeting.sort(key = lambda x:(x[1],x[0])) 
cnt = 1
min_end = meeting[0][1]
for i in range(1,N):
    if meeting[i][0] >= min_end:
        min_end = meeting[i][1]
        cnt += 1

print(cnt)
