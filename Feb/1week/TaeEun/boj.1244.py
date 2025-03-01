N = int(input())
switch_list = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    gender, student = map(int, input().split())
    student -= 1
    if gender == 1:
        for i in range(N):
            if i%student == 0:
                switch_list[i] = 1 - switch_list[i]
    if gender == 2:
        for i in range(N//2):
            if student + N//2 >= N or student - N//2 <0:
                break
            if switch_list[student+i] == switch_list[student-i]:
                switch_list[student+i] = 1 - switch_list[student+i]
                switch_list[student-i] = 1 - switch_list[student-i]

print(switch_list)

#남학생 자기 수가 스위치 번호 배수면 변경
#여학생 자기가 받은 수와 같은 번호가 붙은 스위치 중심으로 좌우가 대칭
#이면서 가장 많은 스위치를 포함하는 구간을 찾아서 바꾼다.


