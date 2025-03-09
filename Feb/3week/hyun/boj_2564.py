'''
0,0을 출발 좌표라 생각하고 좌표에서부터 동서남북의 거리를 구하기
왼쪽 경계, 위 경계 이므로 시계 방향으로 가면 됨
'''
def distance(dir, dist):
    if dir == 1: # 북
        return dist
    elif dir == 2: # 남
        return w + h + (w - dist)
    elif dir == 3: # 서
        return w*2 + h + (h - dist)
    elif dir == 4: # 동
        return w + dist

w, h = map(int, input().split())
N = int(input())
shop = []

# input 값 나누기
for _ in range(N+1):
    # 마지막 줄 전까지 shop 입력받기
    if _ != N:
        shop.append(list(map(int, input().split())))
    else:
        dir, dist = map(int, input().split())

# 최단 거리 합
sum_path = 0

# 동근이의 거리 구하기
dong_path = distance(dir, dist)

for i in range(N):
    # 상점의 거리 구하기
    shop_path = distance(shop[i][0], shop[i][1])
    # 동근이와 상점의 거리는
    # 1. abs(동근 거리 - 상점 거리))
    # 2. 전체 둘레 - abs(동근 거리 - 상점 거리)
    path1 = abs(dong_path - shop_path)
    path2 = 2*(w+h) - path1
    
    if path1 < path2:
        sum_path += path1
    else:
        sum_path += path2

print(sum_path)