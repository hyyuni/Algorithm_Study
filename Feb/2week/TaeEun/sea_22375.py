T=int(input())
for tc in range(1, 1+T):
  N = int(input())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  ans =0

  for i in range(N):
    if A[i] == B[i]:
      continue
    else:
      ans +=1
      for j in range(i, N):
        A[j] = 1-A[j]

  print(f'#{tc} {ans}')

