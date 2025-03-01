# https://www.acmicpc.net/problem/2805

import sys
N, M = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))

if N == 1:
    print(max(0, trees[0] - M))
    sys.exit()  # 바로 종료해서 아래 코드가 실행되지 않도록 함

start, end = 0, max(trees)
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(tree - mid for tree in trees if tree > mid)

    if count < M:
        end = mid - 1
    elif count >= M: # 자를 수 있음. -> 절단기 높이 설정해줘야 한다.
        answer = mid
        start = mid + 1

print(answer)