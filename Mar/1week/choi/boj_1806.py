# 맨처음에는 IM 문제 처럼 풀어봤다 근데 분명 정답일텐데
# 시간 초과가 나길래 IM때도 시간초과때문에 줄여서 줄여서 이렇게 된건데
# 이마저도 시간 초과가 나길래 어떡하지 했는데 
# 문제 아래 알고리즘 분류를 보니 처음보는 단어인 두 포인터라는 말이
# 있길래 구글에 검색해서 투 포인터 알고리즘이란 걸 알게되었다.
##########
# start와 end 지점을 늘리고 줄여주면서 부분합이 S보다 적다면
# 부분합에 arr[end]값을 더해주고 end값을 1 늘려준다
# 부분합이 S보다 크거나 같다면 최솟값을 갱신시켜주고 
# 부분합에 arr[start]값을 빼주고 start값을 1 늘려준다.






N ,S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
sum = 0
min_length = 100000000

while True:
    if sum >= S:
        min_length = min(min_length, end - start)
        sum -= arr[start]
        start += 1
    elif sum < S:
        if end == len(arr):
            break
        sum += arr[end]
        end += 1

if min_length == 100000000:
    print(0)
else:
    print(min_length)