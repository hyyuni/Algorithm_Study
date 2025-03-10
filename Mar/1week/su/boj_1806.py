# 부분합
# https://www.acmicpc.net/problem/1806

import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("swea_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline

# left 0
# 1. 누적합을 구한다. (크기: N+1)
# 2. 길이를 저장할 리스트를 생성한다. (크기: N+1), answer를 저장할 리스트를 생성한다.
#    
# 3. 길이리스트마다 아래 로직을 수행한다.
#    
#    if 누적합[i] - 누적합[left] < S:
#       길이[i] += 1
#       continue

#    if 누적합[i] - 누적합[left] > S: # 
#       <left 조정하기>
#           누적합이 S보다 작아지는 순간, 그 누적합 index보다 한칸이전으로 left 조정하기
#           for j in range(left, i+1):
#               if 누적합[i] - 누적합[j] < S:
#                   left = j - 1
#                   break
#           answer[i]에 추가

#    if 누적합[i] - 누적합[left] == S: 
#       길이[i] += 1
#       answer[i]에 추가

N, S = map(int, input().split())
nums = [0] + list(map(int, input().split()))
INF = int(1e9)
acc_nums = [0] * (N + 1) # 누적합 리스트.
sequence_li = [0] * (N + 1)  # 수열 길이 저장한다. sequence_li[i]: i번째 숫자를 포함했을 때의 최소 수열 길이
answer = [INF] * (N + 1) # S이상일 때의 수열 길이

left = 0

# 누적합 리스트 갱신
for i in range(N+1):
    acc_nums[i] += acc_nums[i-1] + nums[i]

# 현재 i번째 수를 포함했을 때 수열 길이를 계산하며 최소 길이를 찾는다.
for i in range(1, N+1):
    i_sum = acc_nums[i] - acc_nums[left]

    if i_sum < S:
        # 이번 i번째 칸도 수열에 추가한다. 현재 길이 = 이전길이 + 1가 된다. 
        # 다만 아직 S미만이므로 answer리스트를 갱신할 순 없다.
        sequence_li[i] = sequence_li[i-1] + 1  
        
    elif i_sum > S:
        # <left 조정하기>
        # 이번 숫자를 수열에 포함했을 때 S이상이 된다. 
        # 이 때 left를 조정해서 앞쪽의 숫자들을 수열에서 뺀다면, 수열 길이를 최대한 줄일 수 있다.
        
        for l in range(left, i+1):  # 이번 i번째 숫자 1개만으로도 가능할 수 있으므로, range범위는 최대 i+1까지로 해야한다.
            if acc_nums[i] - acc_nums[l] < S:
                left = l - 1
                break

        seq_len = i - left  

        sequence_li[i] = seq_len 
        answer[i] = seq_len

    else:  # 합이 딱 S인 경우
        seq_len = sequence_li[i-1] + 1  # 이번 i번째 칸도 수열에 추가한다. 현재 길이 = 이전길이 + 1가 된다.

        sequence_li[i] = seq_len
        answer[i] = seq_len

answer = min(answer)
print(answer if answer != INF else 0)