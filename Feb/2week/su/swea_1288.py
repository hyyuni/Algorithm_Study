# 새로운 불면증 치료법
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18_yw6I9MCFAZN
def get_result(num):
    digit_n = 10
    showed = [False] * digit_n
    cnt = 1
    all_showed = False
     # 1. 현재 수로 볼 수 있는 양들 체크한다.
    # 2. 다 보게 됐는 지 확인한다.
    while True:
        new_num = num * cnt
 
        # 자리수 체킹하기
        new_nums = list(str(new_num))
        for i in range(len(new_nums)):
            cur_num = int(new_nums[i])
            if not showed[cur_num]:
                showed[cur_num] = True
 
        for i in range(digit_n):
            if not showed[i]:
                break
            if i == digit_n-1 and showed[i]:  # 마지막 자리수까지 다 확인한 경우
            # if showed[digit_n-1]:  # 마지막 자리수까지 다 확인한 경우 -> 이렇게 쓰면 마자막 자리수만 확인하고 끝난다.
                return num * cnt  # 횟수 리턴한다.
 
        cnt += 1
 
 
 
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    answer = -1
    answer = get_result(N)
 
    print(f"#{t} {answer}")