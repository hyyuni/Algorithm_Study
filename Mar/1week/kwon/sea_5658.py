# 보물상자 비밀번호

# 필요 데이터
# 입력 : T, n, n개의 숫자(numbers), k
# password(최종 비밀번호), pass_candi(생성된 숫자 list), 한변에 들어가는 숫자 = n//4

# 1. numbers입력 받기
# 2. 한 칸씩 시계방향 회전
# 3. 필요한 회전 수 = n/4
# 4. 각 변에 들어가는 숫자만큼 잘라서 리스트에 삽입
# 5. 숫자를 내림차순으로 정렬(중복 제거->set 활용)
# 6. 10진수로 변경 후 k 번째 수 찾기

# 16진수 -> 10진수 변환 함수
def hexadecimal_to_decimal(arr):
    alpha = {'A': 10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    decimal = []

    for num in arr:
        stack = []
        for char in num:
            if char.isdigit(): # 숫자일 경우 그대로
                stack.append(int(char)) # 정수 값으로 append
            else:
                 stack.append(alpha[char])   # A-F일 경우 딕셔너리 value 찾기
        result = 0
        i = 0
        while stack:
            result += stack.pop()*(16**i) # 스택에서 뺀 후 16^i 계산
            i += 1
            decimal.append(result)
    decimal.sort(reverse=1) # 내림차수 정렬

    password = decimal[k-1] # k 번째 숫자 찾기
    return password

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    numbers = list(input().strip())
    side = n//4
    pass_candi = set() # 중복 제거를 위해 set 사용

    for i in range(side): # n//4번만큼 시계 방향 회전
        for j in range(0, n, side): # n/4만큼 잘라서 4개 저장
            pass_candi.add("".join(numbers[j:j+side]))
        numbers.insert(0, numbers.pop()) # 마지막 숫자를 맨 앞으로 이동

    print(f'#{tc} {hexadecimal_to_decimal(pass_candi)}')

    # numbers를 n/4 만큼 잘린 4개를 pass_candi 리스트에 삽입
    # for i in range(0,n,side):
    #     candidate = []
    #     for j in range(side):
    #         candidate.append(numbers[i+j])
    #     pass_candi.append(candidate)
    # # print(pass_candi)