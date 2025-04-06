import sys
sys.stdin = open('input.txt', 'r')
'''
우측으로 이동하는 건, 기준점 기준으로 위로 이동
좌측으로 이동하는 건, 기준점 기준으로 아래로 이동

즉,
x가 증가하면 y는 감소
x가 감소하면 y는 증가

아래로 이동하는 건, 기준점 기준으로 우측으로 이동
위로 이동하는 건, 기준점 기준으로 아래로 이동

즉,
y가 증가하면 x는 증가
y가 감소하면 x는 감소
'''

# 방향: 0(→), 1(↑), 2(←), 3(↓)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 드래곤 커브 생성
def dragon_curv(x, y, dir, generation):
    curve = [(x, y)]
    x += dx[dir]
    y += dy[dir]
    curve.append((x, y))

    for _ in range(generation):
        # 드래곤 커브 리스트에서 마지막 좌표 뽑기
        ex, ey = curve[-1]
        for i in range(len(curve)-2, -1, -1):
            cx, cy = curve[i]
            # 90도 회전
            nx = ex - (cy - ey)
            ny = ey + (cx - ex)
            curve.append((nx, ny))

    # arr에 드래곤 커브 입력할 때 좌표 주의하기!
    for cx, cy in curve:
        arr[cy][cx] = 1  # **y: 행, **x: 열

N = int(input())
arr = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y, dir, generation = map(int, input().split())
    dragon_curv(x, y, dir, generation)

# 2x2 정사각형 개수 세기
ans = 0
for y in range(100):
    for x in range(100):
        if arr[y][x] and arr[y][x+1] and arr[y+1][x] and arr[y+1][x+1]:
            ans += 1

print(ans)