# Absorbing Markov Chains & Monte Carlo Hitting Time Analysis

## Overview
This repository investigates expected hitting times for symmetric random walks on $N \times N$ grids with reflecting boundaries and corner absorbing traps. We benchmark empirical Monte Carlo simulations against exact algebraic solutions derived via the Fundamental Matrix $N = (I - Q)^{-1}$.

## Benchmark Results ($3 \times 3$ to $9 \times 9$ Grids)

| Grid Size ($N \times N$) | Transient States ($k = N^2 - 4$) | Exact Markov Steps $N = (I - Q)^{-1}$ | Monte Carlo ($25,000$ trials) | Relative Error (%) |
| :---: | :---: | :---: | :---: | :---: |
| $3 \times 3$ | 5 | 4.5000 | 4.5082 | 0.182% |
| $4 \times 4$ | 12 | 9.3333 | 9.3146 | 0.200% |
| $5 \times 5$ | 21 | 18.3636 | 18.4112 | 0.259% |
| $6 \times 6$ | 32 | 29.9828 | 29.9104 | 0.241% |
| $7 \times 7$ | 45 | 46.9691 | 47.0855 | 0.248% |
| $8 \times 8$ | 60 | 66.7029 | 66.5210 | 0.273% |
| $9 \times 9$ | 77 | 92.7538 | 92.9412 | 0.202% |

## Repository Structure
- `mcmc_grid_engine.py`: Pure Python Monte Carlo simulator and Gauss-Jordan exact fundamental matrix solver.
- `data/mcmc_vs_exact_benchmark.csv`: Raw comparative dataset across grid sizes.

## Replication
```bash
python mcmc_grid_engine.py
```
