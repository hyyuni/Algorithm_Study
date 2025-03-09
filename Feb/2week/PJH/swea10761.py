T = int(input())
for tc in range(1,T+1):
    mid = list(input().split())
    list_o = []
    list_b = []
    seq = []
    N = int(mid[0])

    for i in range(1,len(mid)):
        if i%2==1:
            if mid[i] == 'O':
                list_o.append(int(mid[i+1]))
            else:
                list_b.append(int(mid[i+1]))
        if i%2 ==0:
            seq.append(mid[i])

