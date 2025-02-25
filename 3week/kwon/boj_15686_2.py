# 치킨 배달
def cal_cd(h, c):
    tot = 0
    for i in range(len(h)):
        r1, c1 = h[i]  # r1, c1에 집 좌표 언패킹
        min_distance = float('inf')
        for j in range(len(c)):
            r2, c2 = c[j]  # r2, c2에 치킨집 좌표 언패킹
            distance = abs(r1 - r2) + abs(c1 - c2)
            min_distance = min(min_distance, distance)
        tot += min_distance
    return tot


# 조합 찾기 함수
def chicken_comb(idx, seq):  # 조합을 시작할 인덱스, 현재까지 만들어진 조합
    # 치킨집 수에서 m개의 조합을 선택
    if len(seq) == m:  # 만들어진 조합의 수가 m개 라면,
        unclose.append(seq)  # m개의 좌표를 넣어줌
        return

    else:  # 아니라면
        for i in range(idx, len(chicken)):
            chicken_comb(i + 1, seq + [chicken[i]])  # 현재 만들어진 조합에 치킨 좌표를 추가하면서 조합을 생성


# 입력 받기
n, m = map(int, input().split())
chicken_map = [list(map(int, input().split())) for _ in range(n)]

house = []  # 집 좌표 추가할 리스트
chicken = []  # 치킨집 추가할 리스트

for i in range(n):
    for j in range(n):
        if chicken_map[i][j] == 1:  # 집 추가
            house.append((i, j))
        if chicken_map[i][j] == 2:  # 치킨 집 추가
            chicken.append((i, j))
unclose = []  # 폐업하지 않을 치킨집
if len(chicken) > m:  # 치킨 집 개수가 m보다 크면
    # 치킨 집 중에서 m개의 조합을 찾기
    chicken_comb(0, [])
    min_total_d = float('inf')
    for cases in unclose:
        total_d = cal_cd(house, cases)
        min_total_d = min(min_total_d, total_d)

else:  # 아니라면
    min_total_d = cal_cd(house, chicken)

print(min_total_d)
