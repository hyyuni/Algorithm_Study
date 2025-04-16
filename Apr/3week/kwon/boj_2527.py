# 직사각형
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 겹치지 않는 경우
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        ans = 'd'
    # 점
    elif (x1 == p2 and y1 == q2) or (x1 == p2 and q1 == y2) or (p1 == x2 and q1 == y2) or (p1==x2 and y1 == q2):
        ans = 'c'
    # 선분
    elif (x1 == p2 or p1 == x2) and not (q1 < y2 or q2 < y1):
        ans = 'b'
    elif (y1 == q2 or q1 == y2) and not (p1 < x2 or p2 < x1):
        ans = 'b'
    # 겹치는 부분이 직사각형인 경우
    else:
        ans = 'a'

    print(ans)


    # # 선분
    # if q1 == y2 and (x2 < p1 < p2 or x2 < x1 < p2):
    #     ans = 'b'
    # if x1 == p2 and (y2 < q1 < q2 or y2 < y1 < q2):
    #     ans = 'b'
    # if y1 == q2 and( x2 < x1 < p2 or x2 < p1 < p2):
    #     ans = 'b'
    # if p1 == x2 and (y2 < y1 < q2 or y2 < q1 < q2):
    #     ans = 'b'
    #
    # if y1 == q2 and (x1 < x2 < p1 or x1 < p2 < p1):
    #     ans = 'b'
    # if p1 == x2 and (y1 < y2 < q1 or y1 < q2 < q1):
    #     ans = 'b'
    # if q1 == y2 and (x1 < x2 < p1 or x1 < p2 < p1):
    #     ans = 'b'
    # if x1 == p2 and (y1 < y2 < q1 or y1 < q2 < q1):
    #     ans = 'b'


