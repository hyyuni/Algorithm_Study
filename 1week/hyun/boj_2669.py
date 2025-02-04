import sys
# x,y 좌표가 1이상 100이하인 빈 면적을 만든다
matrix = [[0] * 100 for _ in range(100)] # 2차원 배열 리스트 컴프리헨션
ans= 0

for _ in range(4): # 직사각형 4개의 면적
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2): # 2차원 배열에서 행(세로)과 열(가로)로 처리하는 것이 일반적
        for j in range(x1, x2):
            matrix[i][j] = 1 # 면적 채우기 빈 면적 =  0, 채운 면적 = 1

for square in matrix:
    ans += sum(square) # 위에서 만든 ans 변수에 면적을 모두 더한다

print(ans)