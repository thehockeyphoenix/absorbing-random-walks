import random

def run_random_walk(rows=5, cols=5, trials=10000):
    traps = [(0, 0), (4, 4)]
    total_steps = 0
    trap_counts = {(0, 0): 0, (4, 4): 0}

    for i in range(trials):
        # Start in the middle of the 5x5 grid
        r, c = 2, 2
        steps = 0

        while (r, c) not in traps:
            moves = []
            if r > 0:
                moves.append((r - 1, c)) # up
            if r < rows - 1:
                moves.append((r + 1, c)) # down
            if c > 0:
                moves.append((r, c - 1)) # left
            if c < cols - 1:
                moves.append((r, c + 1)) # right

            r, c = random.choice(moves)
            steps += 1

        total_steps += steps
        trap_counts[(r, c)] += 1

    avg_steps = total_steps / trials
    return avg_steps, trap_counts

avg, counts = run_random_walk()
print("Average steps to get trapped:", round(avg, 2))
print("Times landed in each trap:", counts)
