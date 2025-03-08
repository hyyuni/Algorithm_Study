'''
# 입력 변수
T, N, trees, min_v

# TC당 전략
dfs 백트래킹 홀수, 짝수 날일 때 재귀를 돌기 => 나무에 물을 주거나 물을 안 주기
모든 나무가 tree의 가장 높은 tree에 도달했다면 min과 step을 비교하고 업데이트 해 함수 종료하기 


# dfs 백트래킹으로 구현을 해보려고 했으나 로직 자체에서,
maximum recursion depth가 발생해(1000번 초과) 정답을 구할 수가 없었습니다
내일 다른 로직으로 다시 풀어보겠습니다
'''
import sys
sys.stdin = open('input.txt', 'r')

def dfs(step, day, lst):
    global highest, min_v

    if min(lst) == highest: # 리스트의 모든 요소가 highest에 도달한다면
        min_v = min(min_v, step)
        return
    
    # 물을 안 주고 그냥 지나치기
    dfs(step +1, day+1, lst)

    # 홀수번째 날일 때
    if day % 2 == 1:
        for i in range(len(lst)):
            if lst[i] != highest:
                lst[i] += 1
                dfs(step+1, day+1, lst) # 나무에 물을 주고 재귀
                lst[i] -= 1
                break
        
    # 짝수번째 날일 때
    elif day % 2 == 0:
        for i in range(len(lst)):
            if lst[i] != highest:
                lst[i] += 2
                dfs(step+1, day+1, lst) # 나무에 물을 주고 재귀
                lst[i] -= 2
                break

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    highest = max(trees)
    min_v = float('inf')

    dfs(0, 1, trees)

    print(f'#{tc} {min_v}')