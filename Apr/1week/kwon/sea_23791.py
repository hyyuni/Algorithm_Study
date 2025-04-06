# 지명선수
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    players = [0] * N
    selected = set()

    a_idx = 0
    b_idx = 0
    turn = 0 # 0 : A팀, 1 : B팀

    for _ in range(N):
        if turn == 0: # A팀 차례
            while A[a_idx] in selected: # 해당 선수가 이미 선택되었다면
                a_idx += 1 # 인덱스 + 1
            pick = A[a_idx]
            players[pick -1] ='A'
            selected.add(pick)
        else:
            while B[b_idx] in selected:
                b_idx += 1
            pick = B[b_idx]
            players[pick-1] = 'B'
            selected.add(pick)

        turn = 1 - turn # 순서 변경

    ans = ''.join(players)
    print(ans)
