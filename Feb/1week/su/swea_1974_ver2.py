# 버전2 - dict 사용
import sys
sys.stdin = open("swea_input.txt", "r")
input = sys.stdin.readline

T = int(input())
N = 9
for test_case in range(1, T + 1):
    # print("----------------------------")
    # 중복 숫자 확인하기
        # row 체크
        # column 체크
        # 네모 칸 체크
            # 구역을 나눠서 확인한다.
            # 시작점: (0, 0), (0, 3), (0, 6), (1, 0), (1, 3),  ... 총 9개
            # 시작점 기준으로 3*3 칸 체크
    arr = []
    for i in range(N):
        line = list(map(int, input().split()))
        arr.append(line)

    def check_row_col(arr):
        zipped_by_col = list(zip(*arr))

        for i in range(9):
            if len(arr[i]) != len(set(arr[i])): # row
                return False
            if len(zipped_by_col[i]) != len(set(zipped_by_col[i])): # column
                return False
        return True

    
    def check_cell(arr):
        start_point = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        for start_r, start_c in start_point:
            grid = {}
            for i in range(3):
                for j in range(3):
                    num = arr[start_r + i][start_c + j]
                    if num in grid:
                        return False
                    grid[num] = 1
        return True

    if not check_row_col(arr) or not check_cell(arr):
        print(f"#{test_case} 0")
        continue

    print(f"#{test_case} 1")
    