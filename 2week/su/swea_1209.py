# Sum
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

import sys
sys.stdin = open("swea_input.txt", "r")
input = sys.stdin.readline

T = 10
for t in range(T):
    case_num = int(input())
    arr = []
    row_sum = 0
    col_sum = 0
    for _ in range(100):
        line = list(map(int, input().split()))
        arr.append(line)
    left_d, right_d = 0, 0

    for i in range(100):
        row_sum = max(row_sum, sum(arr[i]))

        temp = 0
        for j in range(100): # 0 ~ 100
            temp += arr[j][i]

            if i == j:
                left_d += arr[i][j]
            
        right_d += arr[i][100-1-i]
        
        col_sum = max(col_sum, temp)

    answer = max(row_sum, col_sum, left_d, right_d)
    print(f"#{t+1} {answer}")
