import sys  # input으로 했더니 시간초과남 ;;;;

stack = []  # 빈리스트 하나 만들기
def push(a):                # 여기부터 함수 5개 만들어놓음 
    stack.append(a)
def pop():
    if stack:
        print(stack.pop())
    else:
        print(-1)
def size():
    print(len(stack))
def empty():
    if stack:
        print(0)
    else:
        print(1)
def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

T = int(sys.stdin.readline().strip())   # 테스트케이스 입력받기

for i in range(T):
    command = sys.stdin.readline().strip().split()  # 테스트케이스만큼 입력받기
    
    if command[0] == "push":    # 입력한 것이 push면 함수 push호출하는데
        push(int(command[1]))   # 유일하게 push만 띄어쓰고 int값이 나오는데 그걸 리스트화 해서 
    elif command[0] == "pop":   # [1]번째의 인트값을 넣어서 push함
        pop()                   # pop호출 
    elif command[0] == "size":  # size호출
        size()
    elif command[0] == "empty": # empty호출
        empty()
    elif command[0] == "top":   # top호출
        top()