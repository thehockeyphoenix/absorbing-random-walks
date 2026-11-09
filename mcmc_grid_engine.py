import numpy as np

def simulate_absorbing_random_walk(grid_size=(5, 5), absorbing_states=[(0, 0), (4, 4)], num_simulations=10000):
    rows, cols = grid_size
    num_states = rows * cols
    
    def state_to_idx(r, c):
        return r * cols + c
        
    def idx_to_state(idx):
        return (idx // cols, idx % cols)
        
    absorbing_indices = [state_to_idx(r, c) for r, c in absorbing_states]
    transient_indices = [i for i in range(num_states) if i not in absorbing_indices]
    
    hitting_times = []
    absorption_counts = {abs_idx: 0 for abs_idx in absorbing_indices}
    
    for _ in range(num_simulations):
        current = transient_indices[len(transient_indices) // 2]
        steps = 0
        while current not in absorbing_indices:
            r, c = idx_to_state(current)
            neighbors = []
            if r > 0: neighbors.append(state_to_idx(r - 1, c))
            if r < rows - 1: neighbors.append(state_to_idx(r + 1, c))
            if c > 0: neighbors.append(state_to_idx(r, c - 1))
            if c < cols - 1: neighbors.append(state_to_idx(r, c + 1))
            
            current = np.random.choice(neighbors)
            steps += 1
            
        hitting_times.append(steps)
        absorption_counts[current] += 1
        
    avg_hitting_time = np.mean(hitting_times)
    return avg_hitting_time, absorption_counts

if __name__ == "__main__":
    avg_steps, abs_counts = simulate_absorbing_random_walk()
    print(f"Average Hitting Time (MCMC): {avg_steps:.4f}")
    print(f"Absorption Distribution: {abs_counts}")

def exact_markov_hitting_time(
    grid_size=(5,5), absorbing_states=[(0,0), (4,4)]):
        rows, cols = grid_size
        
