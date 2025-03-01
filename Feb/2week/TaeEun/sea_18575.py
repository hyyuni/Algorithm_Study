T=int(input())
for tc in range(1, 1+T):
  N = int(input())
  balloon = [list(map(int, input().split())) for _ in range(N)]
  reversed_balloon = [[0]*N for _ in range(N)]
  sum_list = []

  for i in range(N):
    for j in range(N):
      reversed_balloon[j][i] = balloon[i][j]
  
  for i in range(N):
    for j in range(N):
      sum_cross = sum(balloon[i]) + sum(reversed_balloon[j]) - balloon[i][j] 
      sum_list.append(sum_cross)
  ans = max(sum_list) - min(sum_list)
  print(f'#{tc} {ans}')

