import sys
sys.stdin = open("GNS_test_input.txt", "r")
T = int(input())
num_dict = {'ZRO':0,'ONE':1,'TWO':2, 'THR':3,'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
# 버블 정렬
def bubble_sort(arr):
    # 두 개씩 비교해 큰 거 뒤로 보내기
    for i in range(N-1):
        for j in range(N-1):
            if num_dict[arr[j]] > num_dict[arr[j+1]]: # 앞 쪽 요소가 크면 뒤로
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 선택 정렬
def selection_sort(arr):
    # i번째 최솟값 찾아서 i번 요소와 자리 변경
    for i in range(N-1):
        min_idx = i
        for j in range(i,N):
            if num_dict[arr[min_idx]] > num_dict[arr[j]]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 카운팅 정렬
# 1. 요소를 인데그로 활용할 수 있어야 함.
# 2. 최대값과 최소값의 차이가 작아야 효율적
def counting_sort(arr):
    count = [0] * 10
    # 1. 각 요소 개수 세기
    for i in range(N):
        idx = num_dict[arr[i]]
        count[idx] += 1
    # 2. 누적합 구하기(요소가 들어갈 위치 계산)
    for i in range(1, 10):
        count[i] += count[i-1]
    # 3. 각 요소 해당 위치에 넣어주기
    sorted_arr = [None] * N
    for i in range(N):
        # arr[i] 위치 찾기. 위치는 count가 가지고 있고, count의 인덱스는 딕셔너리 활용
        count[num_dict[arr[i]]] -= 1
        # arr[i]가 들어갈 위치 : count[num_dict[arr[i]]]
        position = count[num_dict[arr[i]]]
        sorted_arr[position] = arr[i]
    return sorted_arr
for _ in range(1, T + 1):
    tc, N = map(str, input().split())  # 테스트케이스의 길이(단어의 갯수)
    N = int(N)
    data = input().split()  # 텍스트 입력
    bubble_sort(data)
    selection_sort(data)
    data = counting_sort(data)
    print(tc)
    print(*data)



# sort 메서드
for _ in range(1, T+1):
    tc, N = map(str, input().split()) # 테스트케이스의 길이(단어의 갯수)
    int(N)
    txt_num = list(map(str, input().split())) # 텍스트 입력
    num_dict = {'ZRO':0,'ONE':1,'TWO':2, 'THR':3,'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9} # 딕셔너리설정
    txt_dict = {v:k for k, v in num_dict.items()} # 키 값을 찾기 위해 딕셔러니 뒤집기기
    num_list = []
    for i in range(int(N)):
        num = num_dict.get(txt_num[i]) # 입력된 텍스트로 숫자를 얻어 num_list에 할당
        num_list.append(num) #
    num_list.sort() # 숫자 정렬
    print(f'{tc}', end = ' ')
    for i in range(int(N)):
        txt = txt_dict.get(num_list[i]) # 숫자로 키 값값 찾은 후 출력
        print(txt, end = ' ')