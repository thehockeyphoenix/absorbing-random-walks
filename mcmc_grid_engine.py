import random

def run_random_walk(rows=5, cols=5, trials=10000):
    traps = [(0, 0), (4, 4)]
    total_steps = 0
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
        num_states = rows * cols
        absorbing_indices = [r * cols + c for r, c in absorbing_states]
        transient_indices = [i for i in range(num_states) if i not in absorbing_indices]
  n_trans = len(transient_indices)
        P = np.zeros((num_states, num_states))
  for r in range(rows):
    for c in range(cols):
      curr = r * cols + c
if curr in absorbing_indices:
        P[curr, curr] = 1.0
        continue
      neighbors = []
      if r > 0:
neighbors.append((r - 1, c))
      if r < rows - 1:
        neighbors.append((r + 1, c))
      if c > 0:
        neighbors.append((r, c - 1))
      if c < cols - 1:
        neighbors.append((r, c + 1))
prob = 1.0 / len(neighbors)
      for nr, nc in neighbors:
        P[curr, nr * cols + nc] = prob

Q = P[np.ix_(transient_indices, transient_indices)]
  I = np.eye(n_trans)
  N = np.linalg.inv(I - Q)
hitting_times = N.sum(axis=1)

  start_state = transient_indices[len(transient_indices) // 2]
  print(f"Exact Analytical Hitting Time: {hitting_times[start_state]:.4f}")
if __name__ == "__main__":
  avg_steps, abs_counts = simulate_absorbing_random_walk()
  print(f"Average Hitting Time (MCMC): {avg_steps:.4f}")
  print(f"Absorption Distribution: {abs_counts}")
  exact_markov_hitting_time()
