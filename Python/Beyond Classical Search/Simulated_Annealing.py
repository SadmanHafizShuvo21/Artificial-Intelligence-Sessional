import random, math

N = 8

def conflicts(state):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                count += 1
    return count

def random_state():
    return [random.randint(0, N-1) for _ in range(N)]

def simulated_annealing():
    state = random_state()
    T = 100.0
    cooling = 0.99
    while T > 0.1:
        col = random.randint(0, N-1)
        row = random.randint(0, N-1)
        new_state = state[:]
        new_state[col] = row
        delta = conflicts(new_state) - conflicts(state)
        if delta < 0 or random.random() < math.exp(-delta / T):
            state = new_state
        T *= cooling
    return state

# --- Testcase ---
if __name__ == "__main__":
    solution = simulated_annealing()
    print("Simulated Annealing Solution:", solution)
    print("Conflicts:", conflicts(solution))
