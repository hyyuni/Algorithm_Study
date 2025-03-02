# 경비원
def get_distance(i, j): 
    if i == 1:
        return j
    if i == 2 :
        return x + y + x - j
    if i == 3:
        return x + y + x + y - j
    if i == 4:
        return x + j

x, y = map(int, input().split()) # 가로 세로
n = int(input())
min_dis = 0
store = []

for _ in range(n):
    i, j = map(int, input().split())
    store.append(get_distance(i,j))
dong_x, dong_y = map(int, input().split())
dong = get_distance(dong_x, dong_y)

for i in range(n):
    clockwise = abs(dong-store[i])
    c_clockwise = 2*(x+y) - clockwise # 반시계방향(둘레에서 시계방향 빼주기)
    min_dis += min(clockwise, c_clockwise)
print(min_dis)
#
# def get_coordinates(location, distance):
#     if location == 1: # 북
#         return(y, distance)
#     elif location == 2: # 남
#         return(0, distance)
#     elif location == 3: # 서
#         return(0, y - distance)
#     else:               # 동
#         return(x, y - distance)
#
# x, y = map(int, input().split()) # 가로 세로
# n = int(input())
# stores = [list(map(int, input().split())) for _ in range(n)]
# dong_location, dong_distance = map(int, input().split())
# tot = 0
#
# d_loc, d_dis = get_coordinates(dong_location, dong_distance) # 동근 좌표
#
# for loc, dis in stores:
#     s_loc, s_dis = get_coordinates(loc, dis)
#
#     clockwise = abs(d_loc - s_loc) + abs(d_dis - s_dis)
#     c_clockwise = 2*(x+y) - clockwise # 반시계방향(둘레에서 시계방향 빼주기)
#
#     tot += min(clockwise, c_clockwise)
#
# print(tot)
