# Absorbing Random Walks

A Python simulation project studying 2D absorbing random walks on square grids. A walker starts at the center of an n x n grid and moves randomly up, down, left, or right until it hits an absorbing trap state.

## Files
- `random_walk.py`: Simulates 10,000 walks on a 5x5 grid with traps at `(0, 0)` and `(4, 4)` and tracks average steps and trap distribution.
- `grid_scaling.py`: Runs 5,000 trials across grid sizes from 3x3 to 15x15 to see how average hitting time grows with grid area.
- `trap_placement.py`: Tests asymmetric trap positions on a 5x5 grid by keeping one trap fixed at `(0, 0)` and moving the second trap closer to the center.

## How to Run
```bash
python random_walk.py
python grid_scaling.py
python trap_placement.py
```

## Experiment 1: Grid Scaling Results
Each grid starts the walker at the center `(n // 2, n // 2)` with two opposite corner traps at `(0, 0)` and `(n - 1, n - 1)` over 5,000 trials:

| Grid Size | Total Squares (n^2) | Average Steps to Trap | Steps per Square |
| :--- | :--- | :--- | :--- |
| 3x3 | 9 | 5.97 | 0.66 |
| 5x5 | 25 | 31.42 | 1.26 |
| 7x7 | 49 | 79.98 | 1.63 |
| 9x9 | 81 | 162.11 | 2.00 |
| 11x11 | 121 | 279.62 | 2.31 |
| 13x13 | 169 | 415.58 | 2.46 |
| 15x15 | 225 | 606.94 | 2.70 |

### Observation
As the grid gets larger, the average number of steps grows faster than the total number of squares (n^2). On a 3x3 grid, the walker takes about 0.66 steps per square. By 15x15, that ratio rises to 2.70 steps per square. Increasing the grid area by 25x (from 9 to 225 squares) causes the average hitting time to jump by more than 100x, because in a larger 2D grid the walker has much more room to wander in loops before landing directly on one of the two corner traps.

## Experiment 2: Asymmetric Trap Placement (5x5 Grid)
Starting from the center `(2, 2)`, Trap 1 stays fixed at `(0, 0)` while Trap 2 moves to different positions over 5,000 trials:

| Trap 2 Position | Manhattan Distance from Center | Average Steps to Trap | Hits on Trap 2 |
| :--- | :--- | :--- | :--- |
| `(4, 4)` | 4 | 31.42 | 50.6% |
| `(3, 4)` | 3 | 25.15 | 57.4% |
| `(2, 4)` | 2 | 23.72 | 61.9% |
| `(3, 3)` | 2 | 17.87 | 66.7% |
| `(2, 3)` | 1 | 14.08 | 74.7% |

### Observation
Moving Trap 2 closer to the center cuts the average hitting time by more than half (from 31.42 steps down to 14.08 steps) and shifts the absorption split from roughly 50/50 to nearly 75% in favor of the closer trap. Interestingly, `(2, 4)` and `(3, 3)` are both 2 steps away from the center `(2, 2)`, yet `(3, 3)` catches the walker more often (66.7% vs 61.9%) and faster (17.87 vs 23.72 steps) because `(3, 3)` is an interior cell with 4 entry neighbors while `(2, 4)` sits on the outer edge with only 3.

## Next Steps
- Test directional bias / drift (`biased_walk.py`).
