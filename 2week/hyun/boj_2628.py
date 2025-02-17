column, row = map(int, input().split())
N = int(input())
# 변수 설정
r_lst = [0, row]
c_lst = [0, column]
# 최댓값 변수
r_max = 0
c_max = 0


for _ in range(N):
    temp, n = map(int, input().split())
    # 가로로 자르면 세로값이 짤림
    if temp == 0:
        r_lst.append(n)
    # 세로로 자르면 가로값이 짤림
    else:
        c_lst.append(n)
# 오름차순 정리
r_lst.sort()
c_lst.sort()

# 가장 긴 길이 찾기
for i in range(1, len(r_lst)):
    r_max = max(r_max, r_lst[i] - r_lst[i-1])

for j in range(1, len(c_lst)):
    c_max = max(c_max, c_lst[j] - c_lst[j-1])

print(r_max * c_max)