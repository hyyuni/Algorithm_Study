N = int(input())
switch = list(map(int, input().split()))
student = int(input())

# 학생의 수만큼 반복문 순회
for _ in range(student):
    gen, nums = map(int, input().split())

    if gen == 1: # 남자일 때,
        for i in range(N):
            if (i + 1) % nums == 0: # 남학생 스위치 번호는 자기가 받은 배수이므로
                # + 1을 한 이유는 인덱싱이 0부터 시작하므로
                switch[i] = 1 - switch[i] # 스위치 변경
    else:
        nums -= 1 # 인덱싱이 0부터 시작하므로 여학생의 위치는 -1로 나타남
        left, right = nums, nums 
        while left >= 0 and right < N and switch[left] == switch[right]:
            # 인덱싱 범위가 0 이상 N 미만일 때 왼쪽과 오른쪽 스위치의 값이 같다면
            left -= 1 # 왼쪽으로 범위 이동
            right += 1 # 오른쪽으로 범위 이동

        for i in range(left + 1, right): # 이동한 범위의 값에서 반복문을 돌려
            switch[i] = 1 - switch[i] # 스위치 변경

for i in range(N):
    print(switch[i], end=" ")
    if (i + 1) % 20 == 0: # 출력을 한줄에 20개씩 출력해야 하므로 20으로 나눠떨어짐
        print()
