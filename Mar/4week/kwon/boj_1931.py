# 회의실 배정
# 종료시간 기준으로 오름차순 정렬
# 가장 빨리 끝나는 걸 확정
# 끝난 시간 이후 가장 빨리 끝나는 회의 찾아 확정
import heapq

N = int(input())
heap = []

for i in range(N):
    start, end = map(int, input().split())
    heapq.heappush(heap, (end, start))


cnt = 0
end_time = 0

while heap:
    e, s = heapq.heappop(heap)
    if s >= end_time:
        end_time = e
        cnt += 1
print(cnt)
