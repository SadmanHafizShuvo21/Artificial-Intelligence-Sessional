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

def local_beam(k=3):
    states = [random_state() for _ in range(k)]
    while True:
        if any(conflicts(s) == 0 for s in states):
            return min(states, key=conflicts)
        neighbors = []
        for s in states:
            for col in range(N):
                for row in range(N):
                    if row != s[col]:
                        ns = s[:]
                        ns[col] = row
                        neighbors.append(ns)
        states = sorted(neighbors, key=conflicts)[:k]

# --- Testcase ---
if __name__ == "__main__":
    solution = local_beam(k=4)
    print("Local Beam Search Solution:", solution)
    print("Conflicts:", conflicts(solution))
