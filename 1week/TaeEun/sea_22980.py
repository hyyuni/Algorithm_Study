
def sum_of_squares(n, m=0):
    return (n*(n+1)*(2*n+1) - m*(m-1)*(2*m-1))//6

def sum_a_to_b(b, a=0):
    return (b*(b+1) - a*(a-1))//2
    


def possible_triangle_number(a, b, c, K):

    total = (K+1)*(K+2)*(K+3)//6  #공과 막대 기법으로 생각해보면 모든 수는 K+3 C 3임을 알 수 있음
    sides = [a, b, c]
    invalid_total = 0
    
    for x in sides :
        D = 2*x-(a+b+c)
        m = max(0, -D)
        
        if m > K:
            continue # 만약 긴 변의 최소값 m이 K보다 크면, 불가능한 경우의 수는 0이다.
        d = (K-D)//2
        if d < m:
            d = m-1 # 전환점이 존재하지 않는 경우 그냥 강제로 큰쪽만 발동하게 되게 만들었다
        S1 = (sum_of_squares(d, m) + (2*D+3)*sum_a_to_b(d, m) + (D+1)*(D+2)*(d-m+1))//2
        S2 = (sum_of_squares(K, d+1) - (2*K+3)*sum_a_to_b(K, d+1) + (K+1)*(K+2)*(K-d))//2

        invalid_total += S1+S2
        
    valid = total - invalid_total
    return valid


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b, c, K = map(int, input().split())
    print(possible_triangle_number(a, b, c, K))  
    