import random

def average_hitting_time(n, trials=5000):
    traps = [(0, 0), (n - 1, n - 1)]
    total_steps = 0

    for i in range(trials):
        r, c = n // 2, n // 2
        steps = 0

        while (r, c) not in traps:
            moves = []
            if r > 0:
                moves.append((r - 1, c))
            if r < n - 1:
                moves.append((r + 1, c))
            if c > 0:
                moves.append((r, c - 1))
            if c < n - 1:
                moves.append((r, c + 1))

            r, c = random.choice(moves)
            steps += 1

        total_steps += steps

    return total_steps / trials

grid_sizes = [3, 5, 7, 9, 11, 13, 15]

for size in grid_sizes:
    avg = average_hitting_time(size)
    print(f"{size}x{size} grid -> avg steps: {round(avg, 2)}")
