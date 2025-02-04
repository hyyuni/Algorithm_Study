import sys              ## 얘도 시간초과 걸려서 sys씀 
T = int(sys.stdin.readline().strip())   ## input받고 
empty_list = []                         ## 빈 리스트를 만들어서
for i in range(T):                          
    a = int(sys.stdin.readline().strip())  
    empty_list.append(a)                ## 빈 리스트에 인풋 값 차곡 차곡 쌓아넣기

A = sorted(empty_list)                  ## 정렬하기

for i in range(T):                      ## 0번째부터 출력하면 끄읏읏
    print(A[i])