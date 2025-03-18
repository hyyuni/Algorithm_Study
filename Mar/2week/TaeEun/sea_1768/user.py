from itertools import permutations

query = None

def doUserImplementation(guess):
    candidates = list(permutations(range(10), len(guess)))
    candidates_numbers = 5040

    while candidates_numbers != 1:

        candidates_numbers = len(candidates)
        guessed = candidates[candidates_numbers//2]
        candidates.remove(guessed)

        result = query(guessed)
        balls = result.ball
        strikes = result.strike
        if strikes == 4:
            for i in range(4):
                guess[i] = guessed[i]
            return 

        def strikes_balls(guess):
            remove_list = []

            guess_set = set(guess)
            for candidate in candidates:
                c_strike = 0
                c_ball = 0
                for idx in range(4):
                    if guess[idx] == candidate[idx]:
                        c_strike += 1
                    elif candidate[idx] in guess_set:
                        c_ball += 1
                if c_strike != strikes or c_ball != balls:
                    remove_list.append(candidate)

            return remove_list

        for will_removed in strikes_balls(guessed):
            candidates.remove(will_removed)

    for i in range(4):
        guess[i] = candidates[0][i]

    return 