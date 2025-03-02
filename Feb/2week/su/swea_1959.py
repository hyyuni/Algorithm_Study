# 두개의 숫자열
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())  # len(A), len(B)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
 
    if len(A) >= len(B):
        l_lst, s_lst = A, B
        l_n, s_n = len(A), len(B)
    else:
        l_lst, s_lst = B, A
        l_n, s_n = len(B), len(A)
 
    answer = -1 * int(1e9)
    for i in range(l_n-s_n+1):
        sliced = l_lst[i:i+s_n]  # 짧은 애 길이만큼 자르기
        temp = 0
        for j in range(s_n):
            temp += sliced[j] * s_lst[j]
 
        answer = max(answer, temp)
    print(f"#{t} {answer}")