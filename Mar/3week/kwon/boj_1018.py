N, M = map(int, input().split())
chess = [input().rstrip() for _ in range(N)]

# 체스판의 패턴 정의
white_first = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

min_paint = 64

for j in range(N-7):
    for i in range(M-7):
        count = 0

        for row in range(8):
            for col in range(8):
                if chess[j + row][i + col] != white_first[row][col]:
                    count += 1

        min_paint = min(min_paint, count, 64-count)
        
print(min_paint)