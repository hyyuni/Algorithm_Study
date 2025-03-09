'''
03.08
# 입력 변수
T, N, trees, min_v

# TC당 전략
dfs 백트래킹 홀수, 짝수 날일 때 재귀를 돌기 => 나무에 물을 주거나 물을 안 주기
모든 나무가 tree의 가장 높은 tree에 도달했다면 min과 step을 비교하고 업데이트 해 함수 종료하기 


# dfs 백트래킹으로 구현을 해보려고 했으나 로직 자체에서,
maximum recursion depth가 발생해(1000번 초과) 정답을 구할 수가 없었습니다
'''

'''
03.09
그리디 알고리즘 적용 → 현재 상황에서 최선의 선택을 반복적으로 수행
각 나무가 목표 높이에 도달하기 위해 성장 가능: 홀수 날(1씩 증가)과 짝수 날(2씩 증가)
=> 최소한의 날로 목표 달성을 위해 짝수 날(2씩 증가)을 최대한 활용

1. total = 모든 나무의 성장량 합 (각 나무의 목표 높이까지 필요한 높이 차이의 합)
2. 가능한 한 3일 단위(홀수+짝수)로 성장량을 처리하여 최소 일수 계산
3. 홀수 성장량을 가진 나무가 많다면, 먼저 홀수 날을 배정하고 이후에 짝수 날을 배치하여 최적화
'''
def solve(trees):
    highest = max(trees)
    total = 0  # 나무가 목표 높이까지 자라기 위해 필요한 총 성장량
    odd_growth = 0  # 홀수 성장량이 필요한 나무 개수

    for h in trees:  # 각 나무가 자라야 할 높이를 계산
        needed = highest - h
        total += needed
        if needed % 2 == 1:  # 성장량이 홀수라면 odd_growth 증가
            odd_growth += 1
    
    q, r = divmod(total, 3)  # 총 성장량을 3으로 나눈 몫(q)과 나머지(r)를 구함
    ideal_days = q * 2 + r  # 최적의 최소 일수 계산 (짝수 날을 최대한 활용)
    one_days = (ideal_days + 1) // 2  # 필요한 홀수 날의 개수 계산

    if one_days >= odd_growth:  # 홀수 날이 충분하면 ideal_days 반환
        return ideal_days
    else:  # 홀수 날이 부족하면, 부족한 만큼 추가해서 보정
        return (odd_growth * 2) - 1  # 최소한의 일수 계산

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    
    ans = solve(trees)

    print(f'#{tc} {ans}')


# import sys
# sys.stdin = open('input.txt', 'r')

# def dfs(step, day, lst):
#     global highest, min_v

#     if min(lst) == highest: # 리스트의 모든 요소가 highest에 도달한다면
#         min_v = min(min_v, step)
#         return
    
#     # 물을 안 주고 그냥 지나치기
#     dfs(step +1, day+1, lst)

#     # 홀수번째 날일 때
#     if day % 2 == 1:
#         for i in range(len(lst)):
#             if lst[i] != highest:
#                 lst[i] += 1
#                 dfs(step+1, day+1, lst) # 나무에 물을 주고 재귀
#                 lst[i] -= 1
#                 break
        
#     # 짝수번째 날일 때
#     elif day % 2 == 0:
#         for i in range(len(lst)):
#             if lst[i] != highest:
#                 lst[i] += 2
#                 dfs(step+1, day+1, lst) # 나무에 물을 주고 재귀
#                 lst[i] -= 2
#                 break

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     trees = list(map(int, input().split()))
#     highest = max(trees)
#     min_v = float('inf')

#     dfs(0, 1, trees)

#     print(f'#{tc} {min_v}')