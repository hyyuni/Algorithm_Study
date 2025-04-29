def solution(h1, m1, s1, h2, m2, s2):
    result = 0

    # 시작 시각과 종료 시각을 초로 변환
    t_begin = h1 * 3600 + m1 * 60 + s1
    t_end = h2 * 3600 + m2 * 60 + s2

    # 기준 각도가 0도로 나올 수 있는 0시 또는 12시일 때는 미리 카운트
    if t_begin == 0 or t_begin == 43200:
        result += 1

    while t_begin < t_end:
        # 현재 각도 (시, 분, 초)
        hour_deg_now = (t_begin / 120) % 360
        minute_deg_now = (t_begin / 10) % 360
        second_deg_now = (t_begin * 6) % 360

        # 다음 각도 (시, 분, 초)
        hour_deg_next = (t_begin + 1) / 120 % 360
        if hour_deg_next == 0:
            hour_deg_next = 360

        minute_deg_next = (t_begin + 1) / 10 % 360
        if minute_deg_next == 0:
            minute_deg_next = 360

        second_deg_next = (t_begin + 1) * 6 % 360
        if second_deg_next == 0:
            second_deg_next = 360

        # 초침이 시침을 통과할 때
        if second_deg_now < hour_deg_now and second_deg_next >= hour_deg_next:
            result += 1

        # 초침이 분침을 통과할 때
        if second_deg_now < minute_deg_now and second_deg_next >= minute_deg_next:
            result += 1

        # 세 바늘이 동시에 겹치면 중복 제거
        if second_deg_next == hour_deg_next == minute_deg_next:
            result -= 1

        t_begin += 1

    return result