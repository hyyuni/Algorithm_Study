a, b = map(int, input().split())
c = [a]

while True:
    d = c[-1]
    e = sum(int(f) ** b for f in str(d))
    
    if e in c:
        print(c.index(e))
        break
    
    c.append(e)





'''
입력받은 a값 자리대로 값을 구하기
p제곱을 하고 더한 값을 리스트를 만들어 더하기
만약에 in 리스안에 있는 값이면 바로 i번째 출력후 종료
'''