# 요리사
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH&

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("swea_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline


import itertools
T = int(input())
def get_sum(nums):
    food = 0
    for i in range(len(nums)-1):
        idx_i = nums[i]
        for j in range(i + 1, len(nums)):
            idx_j = nums[j]
            food += matrix[idx_i][idx_j] + matrix[idx_j][idx_i]
    return food

for test_case in range(1, T + 1):
    N = int(input())
    matrix = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    answer = int(1e9)

    nums = [i for i in range(1, N + 1)]

    for group_1 in itertools.combinations(nums, N // 2):
        group_2 = list(set(nums) - set(group_1))
        answer = min(answer, abs(get_sum(group_1) - get_sum(group_2)))

    print(f"#{test_case} {answer}")