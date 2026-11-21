# Absorbing Random Walks

A simple Python simulation of a 2D random walk on a 5x5 grid with two absorbing traps at opposite corners: `(0, 0)` and `(4, 4)`.

## How It Works
- The walker starts at the center of the grid `(2, 2)`.
- At each step, it moves randomly up, down, left, or right (staying inside the grid boundaries).
- The walk ends as soon as it lands on either `(0, 0)` or `(4, 4)`.
- The script runs 10,000 trials to estimate the average number of steps before getting trapped (Monte Carlo method).

## Files
- `random_walk.py`: Runs the 10,000-trial simulation and prints the average hitting time and how often each trap is reached.

## How to Run
```bash
python random_walk.py
