import random

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

def hill_climb():
    state = random_state()
    while True:
        neighbors = []
        for col in range(N):
            for row in range(N):
                if row != state[col]:
                    new_state = state[:]
                    new_state[col] = row
                    neighbors.append(new_state)
        best = min(neighbors, key=conflicts)
        if conflicts(best) >= conflicts(state):
            return state
        state = best

# --- Testcase ---
if __name__ == "__main__":
    solution = hill_climb()
    print("Hill Climbing Solution:", solution)
    print("Conflicts:", conflicts(solution))
