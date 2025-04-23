def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    atk_idx = 0
    continuous_time = 0
    last_attack_time = attacks[-1][0]

    for time in range(1, last_attack_time + 1):
        # 1) 공격 받는 순간 → 회복 스킵, 체력 감소, 연속 초기화
        if atk_idx < len(attacks) and time == attacks[atk_idx][0]:
            health -= attacks[atk_idx][1]
            if health <= 0:
                return -1
            atk_idx += 1
            continuous_time = 0
        else:
            # 2) 붕대 감기에 성공한 초
            continuous_time += 1

            # (a) 매초 기본 회복 x
            health += x
            if health > max_health:
                health = max_health

            # (b) t초 연속 달성 시 보너스 회복 y, 그리고 초기화
            if continuous_time == t:
                health += y
                if health > max_health:
                    health = max_health
                continuous_time = 0

    return health