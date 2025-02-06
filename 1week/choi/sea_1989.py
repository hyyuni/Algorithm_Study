T = int(input())

for tc in range(1, T+1):
    A = input()
    B = A[::-1]
    if A == B:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')