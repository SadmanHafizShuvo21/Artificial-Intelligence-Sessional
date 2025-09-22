N = 8  # Number of queens

def is_safe(state, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for c in range(col):
        r = state[c]
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True

def solve_queens(col=0, state=None, solutions=None):
    if state is None:
        state = [-1] * N
    if solutions is None:
        solutions = []

    if col == N:
        solutions.append(state[:])
        return solutions

    for row in range(N):
        if is_safe(state, row, col):
            state[col] = row
            solve_queens(col + 1, state, solutions)
            state[col] = -1  # backtrack
    return solutions

if __name__ == "__main__":
    sols = solve_queens()
    print(f"Total solutions: {len(sols)}")
    print("Example solution:", sols[0])
