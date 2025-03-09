T = int(input())            # 테스트케이스 
for tc in range(T):
    empty = []              # 빈 리스트 만들기
    a = input()             # 입력받기
    for j in a:
        if j == '(':        # '('가 있으면 j를 empty에 넣기!
            empty.append(j)
        else:               # ')'일때
            if empty:       # empty 리스트가 True면 꺼내서버려버리기
                empty.pop()
            else:           # empty 리스트가 False 즉, 아무것도 없다면 NO 출력하기
                print('NO')
                break       # 끝내기
    else:
        if not empty:       # for 문이 끝났을 때. empty리스트가 False 즉, 비어있으면 YES 출력하기
            print('YES')
        else:               # empty 리스트가 True면 즉, 뭔가 있다면 NO출력
            print('NO')
