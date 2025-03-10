def dfs(v,calorie,point):
    global max_point
    if calorie>L:
        return 
    max_point = max(max_point,point)
    if v == N:
        return
    dfs(v+1,calorie+ham[v][1],point+ham[v][0])
    dfs(v+1,calorie,point)
    

    
T = int(input())
for tc in range(1,T+1):
    N, L = map(int,input().split())
    ham = [list(map(int,input().split())) for _ in range(N)]
    max_point = 0
    dfs(0,0,0)
    print(max_point)



    


