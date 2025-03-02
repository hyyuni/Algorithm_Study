N, M = map(int, input().split())
T = int(input())
store_idx = [list(map(int, input().split()))for _ in range(T)]
dong_idx = list(map(int, input().split()))

answer = 0
answer1 = 0
answer2 = 0
if dong_idx[0] == 1: # 동근이가 북쪽일때
    for i, j in store_idx:
        dj = dong_idx[1]
        if i == 1: # 상점이 북쪽일때
            answer += abs(j - dj)
        elif i == 2: # 상점이 남쪽일때
            answer1 = j + dj + M
            answer2 = (N - dj) + M + (N - j)
            answer += min(answer1, answer2)
        elif i == 3: # 상점이 서쪽일때
            answer += dj + j
        elif i == 4: # 상점이 동쪽일때
            answer += (N - dj) + j
elif dong_idx[0] == 2: # 동근이가 남쪽일때
    for i, j in store_idx:
        dj = dong_idx[1]
        if i == 1: # 상점이 북쪽일때
            answer1 = j + dj + M
            answer2 = (N - dj) + M + (N - j)
            answer += min(answer1, answer2)
        elif i == 2: # 상점이 남쪽일때
            answer += abs(j - dj)
        elif i == 3: # 상점이 서쪽일때
            answer += dj + (M - j) 
        elif i == 4: # 상점이 동쪽일때
            answer += N - dj + (M - j)

elif dong_idx[0] == 3: # 동근이가 서쪽일때
    for i, j in store_idx:
        dj = dong_idx[1]
        if i == 1: # 상점이 북쪽일때
           answer += dj + j
        elif i == 2: # 상점이 남쪽일때
            answer += (M-dj) + j
        elif i == 3: # 상점이 서쪽일때
            answer += abs(j - dj)
        elif i == 4: # 상점이 동쪽일때
            answer1 = N + j + dj 
            answer2 = N + (M - dj) + (M - j)
            answer += min(answer1, answer2)

elif dong_idx[0] == 4: # 동근이가 동쪽일때
    for i, j in store_idx:
        dj = dong_idx[1]
        if i == 1: # 상점이 북쪽일때
           answer += dj + (N - j)
        elif i == 2: # 상점이 남쪽일때
            answer += (M-dj) + (N - j)
        elif i == 3: # 상점이 서쪽일때
            answer1 = N + j + dj 
            answer2 = N + (M - dj) + (M - j)
            answer += min(answer1, answer2)
        elif i == 4: # 상점이 동쪽일때
            answer += abs(j - dj)
print(answer)