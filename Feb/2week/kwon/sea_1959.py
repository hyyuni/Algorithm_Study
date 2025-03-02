# 두 개의 숫자열
# 길이가 짧은 리스트를 이동시켜 마주보는 값들의 곱의 합을 구한 후 최대 값 찾기

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    n_lst = list(map(int, input().split()))
    m_lst = list(map(int, input().split()))
    ans = 0

    u = n if n > m else m # n 과 m 중 큰 수를 u에 할당
    l = n if n < m else m # n과 m 중 작은 수를 l에 할당
    short_lst = n_lst if n < m else m_lst # 길이가 짧은 리스트 찾기
    long_lst = n_lst if n > m else m_lst # 길이가 긴 리스트 찾기

    for i in range(0, u-l+1): # 두 수의 차이만큼 이동
        multy = 0 # 곱 초기화
        for j in range(l): # 작은 수 만큼 반복
            multy += short_lst[j]*long_lst[i+j] # i + j를 통해 긴 리스트의 값 참조
        if ans < multy: # 최대 값 찾기
            ans = multy

    print(f'#{tc} {ans}')