# from itertools import permutations
#
# def count_cases(weights, idx, left_sum, right_sum, remain):
#     global result
#     # 모든 추를 다 놓았을 때 경우의 수 cnt + 1
#     if idx == len(weights):
#         result += 1
#         return
#
#     #  왼쪽보다 크면 종료
#     if right_sum > left_sum + remain:
#         return
#
#     # 추를 왼쪽에 올리는 경우
#     count_cases(weights, idx + 1, left_sum + weights[idx], right_sum, remain - weights[idx])
#
#     # 추를 오른쪽에 올리는 경우
#     if right_sum + weights[idx] <= left_sum: # 왼쪽보다 작을 때
#         count_cases(weights, idx + 1, left_sum, right_sum + weights[idx], remain - weights[idx])
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     weights = list(map(int, input().split()))
#     result = 0
#
#     # 모든 순열에 대해 확인
#     for perm in permutations(weights):
#         count_cases(perm, 0, 0, 0, sum(perm))
#
#     print(f'#{tc} {result}')



from itertools import permutations

def count_cases(weights, idx, left_sum, right_sum, remaining_weight, total_weight):
    global result

    # 모든 추를 다 놓았을 때

    if idx == len(weights):
        result += 1
        return

    # 오른쪽이 왼쪽보다 크면 탐색 종료
    if right_sum > left_sum + remaining_weight:
        return

    # 왼쪽 무게가 전체 절반을 초과하면 남은 경우의 수 추가
    if left_sum > total_weight // 2:
        n = len(weights) - idx  # 남은 추 개수
        result += (2 ** n)  # 남은 추를 올리는 모든 경우의 수 추가
        return

    # 추를 왼쪽에
    count_cases(weights, idx + 1, left_sum + weights[idx], right_sum, remaining_weight - weights[idx], total_weight)

    # 추를 오른쪽
    if right_sum + weights[idx] <= left_sum: # (오른쪽 무게가 왼쪽보다 크지 않을 때만)
        count_cases(weights, idx + 1, left_sum, right_sum + weights[idx], remaining_weight - weights[idx], total_weight)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    result = 0
    total_weight = sum(weights)
    
    for perm in permutations(weights):
        count_cases(perm, 0, 0, 0, sum(perm), total_weight)

    print(f'#{tc} {result}')