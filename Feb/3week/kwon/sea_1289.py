# 원재의 메모리 복구하기

T = int(input())
for test_case in range(1, T+1) :
    memory = list(input())
    count = int(memory.pop(0))
    s = str(count)

    while len(memory) > 0 :
        if s == memory[0] :
            memory.pop(0)
        else:
            s = memory.pop(0)
            count += 1

    print(f'#{test_case} {count}')
