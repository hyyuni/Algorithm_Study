'''
입력변수 = N, S, lst

테케 당 전략
left와 right를 초기 인덱싱으로 설정 (범위 구하기)
=> 이를 투 포인터라고 부른다고 함
while문을 전체 순회했을 때, 즉 left > right 되는 순간 반복문 종료
while문을 순회하면서 left right 범위에서 S이상의 부분합을 구할 수 없다면 바로 반복문 종료
'''
N, S = map(int, input().split())
lst = list(map(int, input().split()))
min_v = float('inf')
left = right = 0
par_sum = 0

while right < N:  # while문 1개만 사용
    par_sum += lst[right]

    if par_sum >= S and left <= right:
        min_v = min(min_v, right - left + 1)
        par_sum -= lst[left]
        left += 1

    right += 1  # right 증가하여 다음 요소 포함

print(min_v)