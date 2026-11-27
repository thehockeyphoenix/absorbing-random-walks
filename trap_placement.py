import random

def test_traps(trap2, trials=10000):
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

    avg_steps = round(total_steps / trials, 2)
    trap2_pct = round((hits[trap2] / trials) * 100, 1)
    return avg_steps, trap2_pct

for r in range(5):
    for c in range(5):
        if (r, c) not in [(0, 0), (2, 2)]:
            steps, pct = test_traps((r, c))
            print(f"Trap 2 at {(r, c)}: avg steps = {steps}, hits trap 2 = {pct}%")
