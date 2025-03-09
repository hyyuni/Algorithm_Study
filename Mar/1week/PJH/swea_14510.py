T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = list(map(int,input().split()))
    cnt = 0
    diff = [0]*N
    one = []
    two = []
    for i in range(N):            #최대 높이와의 차이 구하기
        diff[i] = max(tree)-tree[i]
    for d in diff:
        two += [2]*(d//2)
        if d%2 == 1:
            one.append(1)
    if len(one)>len(two):
        cnt += 2*len(two)
        cnt += 2*(len(one)-len(two))-1
    elif len(one) == len(two):
        cnt += 2*len(one)
    else:
        while len(two)-len(one)>1:
            two.pop()
            one += [1]*2
        cnt += len(one)*2
        cnt += (len(two)-len(one))*2
    print(len(two))
    print(len(one))
    print(f'#{tc} {cnt}')