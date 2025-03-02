N, K = map(int, input().split())  ## 좀 시간이 걸린 이유로는 이항계수가 뭔지 몰랐어서 공식찾으려고 구글링 했씀다.

def factorial(n):                 ## 재귀함수가 저희 월말평가 당시 나왔던게 생각이나서 쓰면서 한번 더 공부하면 좋을 것 같아 써봤습니다.
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
print(int(factorial(N) / (factorial(N-K)*factorial(K))))