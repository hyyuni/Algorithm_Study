# 국회의원 선거
n = int(input())  # 후보 수
d = []
cnt = 0
for i in range(n):
    d.append(int(input()))

if n == 1:
    cnt = 0

else:
    other = d[1:]
    while True:
        max_vote = max(other)
        if d[0] > max_vote:
            break
        d[0] += 1
        max_idx = other.index(max_vote)
        other[max_idx] -= 1
        cnt += 1

print(cnt)