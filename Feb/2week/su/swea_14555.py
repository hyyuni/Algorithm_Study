# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYGtoa3qARcDFARC
# 짝은 딕셔너리에 저장한다. [key: 스택의 최상단 요소]: value: 비교할 현재 문자열
pair = {
    "(": [")", "|"],
    ")": [],
    ".": [],
    "|": [")"]
}
 
T = int(input())
for t in range(1, T+1):
    cnt = 0
    stack = []
    grass = list(input())
    N = len(grass)
    stack.append(grass[0])
 
    for i in range(1, N):
        cur = grass[i]
        if not stack: # 스택 비어있는 경우 예외처리
            stack.append(cur)
            continue
 
        last = stack.pop()
        if cur in pair[last]: # 짝 찾은 경우 (공인 경우)
            cnt += 1
            continue
        stack.append(cur) # 짝이 아닌 경우, stack에 추가한다.
         
    print(f"#{t} {cnt}")