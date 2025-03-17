W, H = map(int, input().split())  # 블록 크기
C = int(input())  # 가게 개수

def convert_pos(d, gap):
    """(방향, 거리) -> 일차원 좌표로 변환"""
    if d == 1:  # 북
        return gap
    elif d == 2:  # 남
        return W + H + (W - gap)
    elif d == 3:  # 서
        return 2 * W + H + (H - gap)
    elif d == 4:  # 동
        return W + gap

# 모든 가게 위치 변환
stores = []
for _ in range(C):
    d, gap = map(int, input().split())
    stores.append(convert_pos(d, gap))

# 동근이 위치 변환
d, gap = map(int, input().split())
dong = convert_pos(d, gap)

# 최단 거리 계산
total_dist = 0
perimeter = 2 * (W + H)  # 전체 둘레

for store in stores:
    dist1 = abs(dong - store)  # 직접 거리
    dist2 = perimeter - dist1  # 반대 방향 거리
    total_dist += min(dist1, dist2)

print(total_dist)
