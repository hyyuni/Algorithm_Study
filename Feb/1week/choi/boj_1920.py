import sys

N = int(sys.stdin.readline())                        ## 시간초과
N_num = set(list(map(int, sys.stdin.readline().split())))   ## 해시태이블을 꼭 이해해야 할 것 같습니다
M = int(input())                                            ## 저번에 강사님께서 해시테이블 얘기를 잠깐하셨는데 list로 했을땐 시간초과가 나던게 set으로 하니 시간복잡도가 거의 확 사라졌습니다.
M_num = list(map(int, sys.stdin.readline().split()))        
for i in M_num:
    if i in N_num:
        print(1)
    else:
        print(0)



