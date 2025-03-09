# 암호생성기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

import sys
sys.stdin = open("swea_input.txt", "r")
input = sys.stdin.readline

T = 10
# T = int(input())

for test_case in range(1, T + 1):
    t_num = int(input())
    nums = list(map(int, input().split()))
    answer = []
    def run_cycle(nums):
        new_nums = nums[:]
        step = 1
        while True:
            if step == 6:
                step = 1
            selected = new_nums.pop(0) 
            selected -= step

            if selected <= 0:
                new_nums.append(0)
                break
            else:
                new_nums.append(selected)
                step += 1
        return new_nums
    
    def decrease(nums, min_num):
        global N
        d_nums = [0] * 8
        q = min_num // N

        # 15로 나눠떨어지는 경우 0처리하기 곤란해짐.. 2번 테케 오류 발생
        # q 보다 한스텝 작은 수로 설정
        if min_num % N == 0:
            q -= 1
        
        for i in range(8):
            d_nums[i] = nums[i] % q
        return d_nums
    
    N = 15
   
    min_num = min(nums)
    if min_num < N:
        answer = run_cycle(nums)
    else:
        nums = decrease(nums, min_num) # 15 배수로 나누기
        answer = run_cycle(nums)

    answer = " ".join(map(str, answer))
    print(f"#{t_num} {answer}")