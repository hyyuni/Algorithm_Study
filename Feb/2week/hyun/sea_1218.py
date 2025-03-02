for tc in range(10):
    N = int(input())
    bracket = list(map(str, input()))
    stack = []

    # 괄호 리스트 생성
    left, right = ['(', '[', '{', '<'], [')', ']', '}', '>']

    for i in range(N):
        if bracket[i] in left:
            # 괄호가 왼쪽 리스트에 있다면 스택에 추가
            stack.append(bracket[i])
        elif bracket[i] in right:
            # 스택이 비어있지 않고, 쌍을 이룬다면
            if stack and right.index(bracket[i]) == left.index(stack[-1]):
                # 맨위의 왼쪽 괄호 pop
                stack.pop()
            else:
                break # 쌍이 아니라면 반복문 종료
    
    # 괄호가 쌍을 만나 모두 제거 된다면 1, 아니면 0 출력
    ans = 1 if len(stack) == 0 else 0

    print(f'#{tc+1} {ans}')