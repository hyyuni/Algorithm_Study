
T = int(input())
N = 4
dx = [0 , 1, 0 ,-1]
dy = [1, 0, -1 ,0 ]


for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for i in range(N)]    

    ans_set = set()
    numbers = [0]*7


    def dfs(x, y, c=0):
        if c == 7:
            ans_set.add(tuple(numbers))
            #numbers가 게속 바뀌니까 값에 저장할 때 튜플로 고정시킨 걸 넣기
            return
        
        numbers[c] = matrix[x][y]

        for i in range(len(dx)):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0<=new_x<N and 0<=new_y<N:
                dfs(new_x, new_y, c+1)



    for x in range(N):
        for y in range(N):
            numbers = [0]*7
            dfs(x, y)
    
    print(f'#{tc} {len(ans_set)}')