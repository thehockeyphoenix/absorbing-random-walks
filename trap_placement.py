import random

def test_traps(trap2, trials=5000):
    traps = [(0, 0), trap2]
    total_steps = 0
    hits = {(0, 0): 0, trap2: 0}

    for i in range(trials):
        r, c = 2, 2
        steps = 0

        while (r, c) not in traps:
            moves = []
            if r > 0:
                moves.append((r - 1, c))
            if r < 4:
                moves.append((r + 1, c))
            if c > 0:
                moves.append((r, c - 1))
            if c < 4:
                moves.append((r, c + 1))

            r, c = random.choice(moves)
            steps += 1

        total_steps += steps
        hits[(r, c)] += 1

    avg_steps = total_steps / trials
    trap2_pct = (hits[trap2] / trials) * 100
    return round(avg_steps, 2), round(trap2_pct, 1)

positions = [(4, 4), (3, 4), (3, 3), (2, 3), (2, 4)]
for pos in positions:
    steps, pct = test_traps(pos)
    print(f"Trap 2 at {pos}: avg steps = {steps}, hits trap 2 = {pct}%")
