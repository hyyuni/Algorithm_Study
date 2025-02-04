
def possible_triangle_number(a, b, c, K):

    total = (K+1)*(K+2)*(K+3)/6  #공과 막대 기법으로 생각해보면 모든 수는 K+3 C 3임을 알 수 있음
    sides = sorted([a, b, c])  # 입력 a, b, c를 정렬 (정렬 후 a <= b <= c)
    a, b, c = sides[0], sides[1], sides[2] #정렬한 걸 다시 a, b, c로 배정
    invalid_total = 0
    
    delta = a + b - c # 초기 삼각형이 유효하다면 delta > 0
    if delta + K <= 0:
        return 0
    # 예시 3번처럼 턱도 없는 값(작은 값 2개 + K < 큰 변)이면 0을 바로 반환

    invalid_total = 0

    valid = total - invalid_total
    return valid


'''
def count_invalid_for_case(delta, K):
    if delta > K:
        return 0
    u0 = (K + delta) // 2
    seg1 = S(u0 - delta)
    seg2 = S(K - (u0 + 1))
    return seg1 + seg2

def count_valid_outcomes_closed(A, B, C, K):

    a, b, c = sorted([A, B, C])
    delta = a + b - c
    if delta + K <= 0:
        return 0
    total = (K + 1) * (K + 2) * (K + 3) // 6
    
    # Case X: 최대가 X = a+u, δ₁ = (b+c) - a.
    delta1 = (b + c) - a
    inv_x = count_invalid_for_case(delta1, K)
    
    # Case Y: 최대가 Y = b+v, δ₂ = (a+c) - b.
    delta2 = (a + c) - b
    inv_y = count_invalid_for_case(delta2, K)
    
    # Case Z: 최대가 Z = c+w, δ₃ = (a+b) - c.
    delta3 = (a + b) - c
    inv_z = count_invalid_for_case(delta3, K)
    
    total_invalid = inv_x + inv_y + inv_z
    valid = total - total_invalid
    return valid
'''


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b, c, K = map(int, input().split())
    print(possible_triangle_number(a, b, c, K))  
    
