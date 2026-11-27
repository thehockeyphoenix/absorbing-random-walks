# Absorbing Random Walks

A Python simulation project studying 2D absorbing random walks on square grids. A walker starts at the center of an n x n grid and moves randomly up, down, left, or right until it hits an absorbing trap state.

## Files
- `random_walk.py`: Simulates 10,000 walks on a 5x5 grid with traps at `(0, 0)` and `(4, 4)` and tracks average steps and trap distribution.
- `grid_scaling.py`: Runs 5,000 trials across grid sizes from 3x3 to 15x15 to see how average hitting time grows with grid area.
- `trap_placement.py`: Sweeps all 23 valid positions for Trap 2 on a 5x5 grid (10,000 trials each) while keeping Trap 1 fixed at `(0, 0)`.

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

## Experiment 2: Full 5x5 Trap Placement Sweep
Starting from the center `(2, 2)`, Trap 1 stays fixed at `(0, 0)` while Trap 2 is tested on every other square (10,000 trials per square). Each cell shows `avg steps (Trap 2 hit %)`:

| Row \ Col | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Row 0** | Trap 1 | 45.76s (71.2%) | 33.27s (67.5%) | 30.84s (60.0%) | 35.94s (50.5%) |
| **Row 1** | 45.62s (71.7%) | 29.48s (83.3%) | 18.73s (82.6%) | 20.93s (70.7%) | 27.61s (59.0%) |
| **Row 2** | 34.21s (67.5%) | 18.73s (83.3%) | Start | 14.04s (76.2%) | 23.50s (62.5%) |
| **Row 3** | 31.24s (59.0%) | 21.48s (69.4%) | 14.09s (75.2%) | 17.48s (67.8%) | 24.96s (58.9%) |
| **Row 4** | 36.17s (50.2%) | 27.67s (59.0%) | 23.55s (62.1%) | 25.21s (57.7%) | 31.58s (50.4%) |

### Key Observations
1. **Diagonal symmetry check:** Because both `(0, 0)` and `(2, 2)` lie on the main diagonal, swapping row and column coordinates should give the same result. The simulation confirms this: `(0, 1)` vs `(1, 0)` (45.76 vs 45.62 steps) and `(2, 3)` vs `(3, 2)` (14.04 vs 14.09 steps) match closely, showing that 10,000 trials keeps sampling noise low.
2. **Corner 50/50 split vs. coverage:** Placing Trap 2 in any of the other three corners (`(0, 4)`, `(4, 0)`, or `(4, 4)`) keeps the capture split right around 50% because all four corners are 4 grid steps from the center. However, opposite corners `(4, 4)` finish faster (31.58 steps) than adjacent corners `(0, 4)` or `(4, 0)` (~36.0 steps) because opposite corners cover both sides of the grid.
3. **Shielding vs. speed:** Both `(1, 2)` and `(2, 3)` are 1 step from the center. Placing Trap 2 at `(2, 3)` gives the fastest overall absorption on the grid (14.04 steps, 76.2% hits). Placing it at `(1, 2)` increases Trap 2's share to 82.6% because it sits between the center and `(0, 0)` and intercepts walkers heading toward Trap 1, but average steps jump to 18.73 because the bottom-right region is left open.
4. **The `(1, 1)` chokepoint:** Even though `(1, 1)` is 2 steps from the center, it achieves the highest capture share on the grid (83.3%). To reach `(0, 0)`, a walker must pass through `(0, 1)` or `(1, 0)`, and `(1, 1)` sits directly next to both of those entry cells.
5. **Slowest setup:** Clustering both traps in the same corner (`(0, 0)` and `(0, 1)`) produces the longest walks (~45.7 steps), since the rest of the 5x5 grid has no trap at all.

## Next Steps
- Test directional bias / drift (`biased_walk.py`).
