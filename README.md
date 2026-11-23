# Absorbing Random Walks

A Python simulation project studying 2D absorbing random walks on square grids. A walker starts at the center of an n x n grid and moves randomly up, down, left, or right until it hits an absorbing trap state.

## Files
- `random_walk.py`: Simulates 10,000 walks on a 5x5 grid with traps at `(0, 0)` and `(4, 4)` and tracks average steps and trap distribution.
- `grid_scaling.py`: Runs 5,000 trials across grid sizes from 3x3 to 11x11 to see how average hitting time grows with grid area.

## How to Run
```bash
python random_walk.py
python grid_scaling.py
```

## Experiment 1: Grid Scaling Results
Each grid starts the walker at the center `(n // 2, n // 2)` with two opposite corner traps at `(0, 0)` and `(n - 1, n - 1)` over 5,000 trials:

| Grid Size | Total Squares (n^2) | Average Steps to Trap |
| :--- | :--- | :--- |
| 3x3 | 9 | 6.02 |
| 5x5 | 25 | 31.41 |
| 7x7 | 49 | 80.85 |
| 9x9 | 81 | 157.92 |
| 11x11 | 121 | 265.40 |

### Key Observation
Average hitting time grows faster than the total number of squares (n^2). Increasing the grid from 3x3 to 9x9 increases the area by 9x, while the average number of steps increases by more than 26x (matching the expected n^2 log(n) scaling behavior of 2D random walks).

## Next Steps
- Test asymmetric trap placements on a 5x5 grid (`trap_placement.py`).
- Test directional bias / drift (`biased_walk.py`).
