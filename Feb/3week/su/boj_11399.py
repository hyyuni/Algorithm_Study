# ATM
# https://www.acmicpc.net/problem/11399
import sys

N = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().strip().split()))
sum_times = [0] * N
times.sort()
for i in range(N):
    if i == 0:
        sum_times[0] = times[i]
        continue
    sum_times[i] = sum_times[i-1] + times[i]

print(sum(sum_times))