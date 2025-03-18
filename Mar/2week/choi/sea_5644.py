
T = int(input())
def get_available_chargers(x, y):
        available = []
        for idx, charger in enumerate(chargers):
            cx, cy, c, p = charger
            if abs(x - cx) + abs(y - cy) <= c:
                available.append((p, idx))
        return available    
def haha():
    a_pos = (0, 0)
    b_pos = (9, 9)

    directions = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)] # X, 상, 우, 하, 좌

    total_charge = 0

    a_chargers = get_available_chargers(a_pos[0], a_pos[1])
    b_chargers = get_available_chargers(b_pos[0], b_pos[1])
    if a_chargers and b_chargers:
        max_charge = 0
        for a_p, a_idx in a_chargers:
            for b_p, b_idx in b_chargers:
                if a_idx == b_idx:
                    max_charge = max(max_charge, a_p)
                else:
                    max_charge = max(max_charge, a_p + b_p)
        total_charge += max_charge
    else:
        if a_chargers:
            total_charge += max([p for p, idx in a_chargers])
        if b_chargers:
            total_charge += max([p for p, idx in b_chargers])

    for i in range(M):
        a_pos = (a_pos[0] + directions[user_a[i]][0], a_pos[1] + directions[user_a[i]][1])
        b_pos = (b_pos[0] + directions[user_b[i]][0], b_pos[1] + directions[user_b[i]][1])
        a_chargers = get_available_chargers(a_pos[0], a_pos[1])
        b_chargers = get_available_chargers(b_pos[0], b_pos[1])

        if a_chargers and b_chargers:
            max_charge = 0
            for a_p, a_idx in a_chargers:
                for b_p, b_idx in b_chargers:
                    if a_idx == b_idx:
                        max_charge = max(max_charge, a_p)
                    else:
                        max_charge = max(max_charge, a_p + b_p)
            total_charge += max_charge
        else:
            if a_chargers:
                total_charge += max([p for p, idx in a_chargers])
            if b_chargers:
                total_charge += max([p for p, idx in b_chargers])
    print(f"#{tc} {total_charge}")
    

for tc in range(1, T + 1):
    M, A = map(int, input().split())
    user_a = list(map(int, input().split()))
    user_b = list(map(int, input().split()))
    chargers = []
    for _ in range(A):
        x, y, c, p = map(int, input().split())
        chargers.append((x - 1, y - 1, c, p))
    haha()
        
