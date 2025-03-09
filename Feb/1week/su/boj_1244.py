# import sys
# sys.stdin = open("input_2.txt", "r")

S = int(input())
arr = ["_"] + list(map(int, input().split())) # 스위치 상태
students = int(input())

def toggled(num):
    if num == 1:
        return 0
    elif num == 0:
        return 1

for stu in range(students):
    gender, given = map(int, input().split()) # 1:남, 2: 여
    if gender == 1:
        for i in range(given, S+1, given):
            arr[i] = toggled(arr[i])
    elif gender == 2:
        arr[given] = toggled(arr[given])
        step = 1
        while True:
            left, right = given - step, given + step
            if left <= 0 or right >= S+1:
                break
            if arr[left] == arr[right]:
                toggled_num = toggled(arr[left])
                arr[left], arr[right] = toggled_num, toggled_num
                step += 1
            else:
                break


for i in range(1, S+1, 20):
    print(*arr[i:i+20])