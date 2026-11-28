import random

def biased_walk(weight_rd, trials=5000):
    traps = [(0, 0), (4, 4)]
    total_steps = 0
    hits = {(0, 0): 0, (4, 4): 0}

    for i in range(trials):
        r, c = 2, 2
        steps = 0

        while (r, c) not in traps:
            moves = []
            if r > 0:
                moves.append((r - 1, c))
            if r < 4:
                moves.extend([(r + 1, c)] * weight_rd)
            if c > 0:
                moves.append((r, c - 1))
            if c < 4:
                moves.extend([(r, c + 1)] * weight_rd)

            r, c = random.choice(moves)
            steps += 1

        total_steps += steps
        hits[(r, c)] += 1

    avg_steps = round(total_steps / trials, 2)
    pct_44 = round((hits[(4, 4)] / trials) * 100, 1)
    return avg_steps, pct_44

for w in [1, 2, 3, 4]:
    steps, pct = biased_walk(w)
    print(f"Weight {w}: avg steps = {steps}, hits (4, 4) = {pct}%")
