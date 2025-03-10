def hehe():
    global arr
    a = N // 4
    for i in range(4):
        arr.append(chest[a*i : a*(i+1)])
    pass
 
 
 
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    chest = list(input())
    arr = []
    hex = []
    hehe()
    for i in range(len(arr[0])-1):
        a = chest.pop(0)
        chest.append(a)
        hehe()
    arr = list(map(list, (set(map(tuple, arr)))))
    arr = ["".join(a) for a in arr]
    for i in arr:
        a = int(i, 16)
        hex.append(a)
    res = sorted(hex, reverse = True)
    print(f'#{tc} {res[K-1]}')