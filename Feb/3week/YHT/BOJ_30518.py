import itertools

def winner(a, b):
    if a == b: return "D"  # 비김
    if (a == "R" and b == "S") or (a == "S" and b == "P") or (a == "P" and b == "R"):
        return "L"  # 패배
    return "W"  # 승리

def count_valid(first, small):
    n, mod, cnt = len(small), 1_000_000_007, 0

    for length in range(1, n + 1):
        for idx in itertools.combinations(range(n), length):
            small_sub = [small[j] for j in idx]  # 부분 문자열 생성
            light = [first] + small_sub[:-1]  # lighter는 smallant 따라야 함

            valid = True
            for k in range(len(light) - 1):  # 관중이 분노하는 상황 체크
                if winner(light[k], small_sub[k]) == "L" and light[k + 1] == small_sub[k + 1]:
                    valid = False
                    break

            if valid:
                cnt = (cnt + 1) % mod

    return cnt

# 입력
first = input().strip()
moves = input().strip()

# 결과 출력
print(count_valid(first, moves))
