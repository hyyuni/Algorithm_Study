T = int(input())

for tc in range(1, T+1):
    A = list(map(int, input().split()))
    maxA = -1
    minA = 100000
    for _ in A:
        if maxA < _:
            maxA = _
        elif minA > _:
            minA = _
        else:
            pass
    idxmaxA = A.index(maxA)
    A.pop(idxmaxA)
    
    idxminA = A.index(minA)
    A.pop(idxminA)
    C = A
    D = round(sum(A) / len(A))
    print(D)
    print(f'#{tc} {D}')