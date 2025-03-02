N = int(input())
status = list(map(int, input().split()))
status_div = len(status) // 2
num_of_stu = int(input())
for i in range(1, num_of_stu + 1):
    gender, number = map(int, input().split())
    number_div = (N // number)
    if gender == 1:
        for j in range(1, number_div+1):
            if status[number * j-1] == 1:
                status[number * j-1] = 0
            else:
                status[number * j-1] = 1
    else:
        if status[number-1] == 0:
            status[number-1] = 1
        else:
            status[number-1] = 0
        for k in range(1, status_div+1):
            if 0 <= number-k-1 < N and 0 <= number+k-1 < N:
                if status[number+k-1] == status[number - k-1]:
                    if number-k-1 >= 0:
                        if status[number+k-1] == 1:
                            status[number+k-1] = 0
                            status[number-k-1] = 0
                        else:
                            status[number+k-1] = 1
                            status[number-k-1] = 1
                    else:
                        break
                else:
                    break
for i in range(0, N, 20):
    print(" ".join(map(str, status[i:i+20])))