T = int(input())
for tc in range(1, T+1):
    N = int(input())
    list_a = [[0] * N for _ in range(N)]
    
    i, j = 0, 0  
    val = 1
    list_a[i][j] = val

    direction = 0  

    while val < N * N:
        if direction == 0:  
            if j + 1 < N and list_a[i][j + 1] == 0:
                j += 1
            else:
                direction = 1  
                i += 1
        elif direction == 1:  
            if i + 1 < N and list_a[i + 1][j] == 0:
                i += 1
            else:
                direction = 2  
                j -= 1
        elif direction == 2:  
            if j - 1 >= 0 and list_a[i][j - 1] == 0:
                j -= 1
            else:
                direction = 3  
                i -= 1
        elif direction == 3:  
            if i - 1 >= 0 and list_a[i - 1][j] == 0:
                i -= 1
            else:
                direction = 0  
                j += 1

        val += 1
        list_a[i][j] = val

    print(f'#{tc}')
    for row in list_a:
        print(*row)

# T = int(input())
# di = [0,1,0,-1]
# dj = [1,0,-1,0]
# for tc in range(1,T+1):
#     N = int(input())
#     list_a = [[0]*N for _ in range(N)]
#     i = 0
#     j = 0
#     val = 1
#     dr = 0
#     list_a[i][j] = val
#     val += 1

#     while val<=N*N:
#         ni,nj = i+di[dr], j+dj[dr]
#         if 0<=ni<N and 0<=nj<N and list_a[ni][nj]==0:
#             i, j = ni, nj
#             list_a[i][j] = val
#             val += 1
#         else:
#             dr = (dr+1)%4

#     print(f'#{tc}')
#     for lst in list_a:
#         print(*lst)