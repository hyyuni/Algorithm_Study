# 공 넣기
N, M = map(int, input().split()) # N : 바구니 개수 M : 공을 넣는 횟수
bucket = [0]*N # 바구니에 N개 만큼 0 리스트 삽입

for x in range(M):
    i, j, k = map(int, input().split()) # i: 첫번쨰 j : 마지막 k: 공번호
    for y in range(i-1, j):
        bucket[y] = k #i-1번 리스트부터 j-1리스트까지 k 삽입

for balls in bucket:
    print(f'{balls}', end = ' ')

# for _ in range(N): # 바구니에 N개 만큼 0 리스트 삽입
    #     bucket.append(0)
    # for y in range(i - 1, j):
    #     bucket.insert(y, k)  # i-1번 리스트부터 j-1리스트까지 k 삽입
    
