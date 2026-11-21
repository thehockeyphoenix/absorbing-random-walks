import random

def run_random_walk(rows=5, cols=5, trials=10000):
    traps = [(0, 0), (4, 4)]
    total_steps = 0
    trap_counts = {(0, 0): 0, (4, 4): 0}

  
