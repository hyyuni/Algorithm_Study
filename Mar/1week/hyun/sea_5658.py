'''
# 입력변수
T, N, K

1. 16진수 A = 10, B = 11, C = 12, D = 13, E = 14, F = 15, 16 = 10
2. def rotate 함수 = 배열을 한 칸씩 회전시켜야 함
[nums[-1]] + nums[:-1] # 마지막 요소를 맨 앞으로 이동
'''
import sys
sys.stdin = open('input.txt', 'r')

def rotate_num():
    return [nums[-1]] + nums[:-1] # 마지막 요소 맨 앞으로 이동


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(input())
    nums_set = set() # 생성 가능한 수를 내림 차순 나열했을 때, 중복 방지

    for _ in range(N//4):
        for i in range(0, N, N//4):
            hex_num = ''.join(nums[i:i+N//4])
            nums_set.add(int(hex_num, 16))
        nums = rotate_num() # 비밀 번호 생성 후 리스트 회전
    box_pw = sorted(nums_set, reverse=True) # 내림차순 정렬
    ans = box_pw[K-1]

    print(f'#{tc} {ans}')