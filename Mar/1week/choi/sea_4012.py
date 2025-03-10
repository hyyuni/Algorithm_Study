# 함수정의할거임 음식합하는
# def 합 함수(arr, abc):
#   res = 0
#   for i, j in combinations(abc, 2) -> 2개씩 뺄거임 why? 두개의 인덱스가 필요하니까.
#       res += arr[i][j] + arr[j][i]
#   return res
# 2중 조합을 만들거임. 
# 조합을 할거임.        N = 6
# for 뭐시기 in combination(range(N) , N / 2) # 어차피N은 짝수로 나옴.
    # 여기서 반을 갈라야하는데.. 어떻게 갈라야 할지 모르겠음 여튼 그걸 반 나눔. ...이거 아눈사람 알려주셈,,,
    # why? -> 요리를 두개 만들어야하니까.
    # 나눈걸 예를들어 A, B라고 해보자.
    #   위 함수 호출할거야
    # ans1 = 합(arr, A)
    # ans2 = 합(arr, B)
    # real_ans = min(res, abs(ans1-ans2))
# 다 끝나면 real_ans 출 력!






from itertools import combinations

def sum_food(arr, abc):
    res = 0
    for i, j in combinations(abc, 2):
        res += arr[i][j] + arr[j][i]
    return res

T = int(input())
for tc in range(1, T+1):
    N = int(input()) 
    arr = [list(map(int, input().split()))for _ in range(N)]
    res = 100000000
    for ca1 in combinations(list(range(N)), N // 2):
        ca2 = set(range(N))-set(ca1)
        ans1 = sum_food(arr, ca1)
        ans2 = sum_food(arr, ca2)
        res = min(res, abs(ans2 - ans1))
    print(f'#{tc} {res}')