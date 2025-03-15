import sys
from user import doUserImplementation, query  # query will be replaced with our API


N = 4
MAX_QUERYCOUNT = 1000000
limit_query = 2520

# 전역 변수들
digits = [0] * N
digits_c = [0] * 10
querycount = 0


class Result:
    def __init__(self, strike=0, ball=0):
        self.strike = strike
        self.ball = ball


def isValid(guess):
    if len(guess) != N:
        return False
    guess_c = [0] * 10
    for num in guess:
        if num < 0 or num >= 10 or guess_c[num] > 0:
            return False
        guess_c[num] += 1
    return True


def query_api(guess):
    """
    API 함수: guess와 secret digits (digits, digits_c)를 비교하여 strike, ball 정보를 반환한다.
    """
    global querycount, digits, digits_c
    if querycount >= MAX_QUERYCOUNT:
        return Result(-1, -1)
    querycount += 1

    if not isValid(guess):
        return Result(-1, -1)

    strike = 0
    ball = 0
    for idx in range(N):
        if guess[idx] == digits[idx]:
            strike += 1
        elif digits_c[guess[idx]] > 0:
            ball += 1

    return Result(strike, ball)


def initialize():
    """
    입력 스트림에서 4개의 숫자(0~9)를 읽어 secret digits를 초기화한다.
    C 코드와 같이 digit 이외의 문자는 건너뛴다.
    """
    global digits, digits_c, querycount
    digits_c = [0] * 10

    s = ""
    # 4개의 숫자를 모을 때까지 계속 읽음 (공백, 개행 등 무시)
    while len(s) < N:
        line = sys.stdin.readline()
        if not line:
            break
        # line 내의 모든 숫자만 골라내기
        s += "".join(ch for ch in line if ch.isdigit())
    if len(s) < N:
        # 만약 부족하다면 0으로 채운다.
        s = s.ljust(N, "0")
    digits = [int(ch) for ch in s[:N]]
    for d in digits:
        digits_c[d] += 1
    querycount = 0


def check(guess):
    """현재 guess가 secret digits와 정확히 일치하는지 확인"""
    return guess == digits


def main():
    global querycount
    # 첫 줄은 테스트 케이스 수 T
    T_line = sys.stdin.readline()
    if not T_line:
        return
    try:
        T = int(T_line.strip())
    except ValueError:
        return

    total_score = 0
    total_querycount = 0

    # user 모듈 내부에서 query 함수를 사용하도록 업데이트 (API 연결)
    import user
    user.query = query_api

    for testcase in range(1, T + 1):
        initialize()
        guess = [0] * N  # 사용자가 채워넣을 배열

        # 사용자 구현 함수 호출
        doUserImplementation(guess)

        # 만약 최종 guess가 secret과 다르다면, querycount를 최대값으로 처리
        if not check(guess):
            querycount = MAX_QUERYCOUNT

        if querycount <= limit_query:
            total_score += 1

        print(f"#{testcase} {querycount}")
        total_querycount += querycount

    if total_querycount > MAX_QUERYCOUNT:
        total_querycount = MAX_QUERYCOUNT
    print(f"total score = {total_score * 100 // T}")
    print(f"total query = {total_querycount}")


if __name__ == "__main__":
    main()
