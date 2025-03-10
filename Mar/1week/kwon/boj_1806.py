# 부분합

# 합이 s보다 작을시 -> end idx +1 (연산 값이 커져야하므로), 구간의 합을 sum에 더하기
# 합이 s보다 클 시 -> 구간의 길이를 result에 추가, start idx +1 하면서 합을 더하고, 합이 s 이상인지 확인

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = 0, 0
result = []
sum = numbers[0]

while True:
    if sum < s:
        end += 1
        if end < 0 or end >= n:
            break
        sum += numbers[end]

    elif sum >= s:
        result.append(end-start+1)
        sum -= numbers[start]
        start += 1
        if start < 0 or start >= n:
            break


print(0 if len(result) == 0 else min(result)) # 합을 구할 수 있으면 최소 값, 구할 수 없으면 0 출력