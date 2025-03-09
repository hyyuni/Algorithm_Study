# 나무 높이

# 필요 데이터
# 입력 : T, N, tree(초기높이)
# 출력 : tc, min_date
# date, max_tree, diff, even, odd

# 가장 크기가 큰 나무 높이 구하기
# 각 나무와 가장 큰 나무 높이와의 차이 구하기
# 짝수 차이, 홀수 차이 따로 계산
# 1 차이 날 때까지 매일 최대한 2씩 성장

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 나무의 개수
    tree = list(map(int, input().split()))
    diff = []

    even = 0 # 2씩 주는 날
    odd = 0  # 1씩 주는 날

    max_tree = max(tree) # 가장 큰 나무 높이 구하기

    for i in range(N):
        diff.append(max_tree - tree[i])

    for i in range(len(diff)):
        even += diff[i] // 2 # 2씩 주는 횟수
        odd += diff[i] % 2 # 1 씩 주는 횟수

    max_days = max(even, odd) # 총 필요한 날짜 계산
    # 짝수와 홀수 중 더 큰 값을 최소 날짜로 설정

    additional = (max_days - even) * 2 # 1을 줘야하는 날
    # 홀수 차이와 짝수 차이를 비교하여 부족한 부분을 보정

    answer = max_days * 2 - (additional // 2)
    # 최악의 경우 max_days * 2를 가정하고, additional을 반영하여 최소 날짜 찾기
    print(f'#{tc} {answer}')