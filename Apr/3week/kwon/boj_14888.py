# 연산자 끼워넣기
def dfs(depth, total, plus, minus, multiply, divide):
    global max_ans, min_ans
    if depth == N:
        max_ans = max(max_ans, total)
        min_ans = min(min_ans, total)
        return
    if plus:
        dfs(depth + 1, total + A[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - A[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * A[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / A[depth]), plus, minus, multiply, divide - 1)

N = int(input())
A = list(map(int,input().split()))
op = list(map(int, input().split())) # +, -, *, //

max_ans = -float('inf') # 음수만 나오는 tc가 있을 수 있으므로
min_ans = float('inf')

dfs(1, A[0], op[0], op[1], op[2], op[3])

print(max_ans)
print(min_ans)



# 처음에 max_ans = 0으로 놓고 문제를 풀어서 틀림 ㅜㅜ
# 문제의 조건이 -10억 ~ 10억 이므로 
# max_ans = -float('inf')로 정해 해결함 
