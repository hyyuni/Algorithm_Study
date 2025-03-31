import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

meetings = [] # 회의 시간을 저장할 리스트
cnt = 0 # 사용할 수 있는 회의 카운트하기
finished_time = 0 # 회의 종료 시간 업데이트할 변수 

for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s,e))

# 힌트: (1,4), (5,7), (8,11), (12,14) 를 이용할 수 있다. (종료 시간이 다른 회의와 겹치지 않는 규칙 발견!)
# 회의를 '종료 시간 기준'으로 오름차순 정렬하면, 이후 회의와 겹치지 않는 최적의 선택(Greedy)를 할 수 있음
# lambda 함수를 활용하자!

meetings.sort(key=lambda x: (x[1], x[0]))
# case1번 출력 값,
# [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

for s, e in meetings:
    if s >= finished_time:
        finished_time = e
        cnt += 1

print(cnt)


# 런타임 에러 (시간 제한 2초)
'''
def dfs(idx, finished_time, cnt):
    global ans
    
    # 모든 회의를 확인한 경우
    if idx == N:
        ans = max(ans, cnt)
        return
    
    s, e = meetings[idx]
    
    # 현재 회의를 선택하는 경우
    if s >= finished_time:
        dfs(idx + 1, e, cnt + 1)
    
    # 현재 회의를 선택하지 않는 경우
    dfs(idx + 1, finished_time, cnt)

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
dfs(0, 0, 0)

print(ans)
'''