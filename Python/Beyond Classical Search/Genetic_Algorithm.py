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

def genetic(pop_size=50, generations=1000, mutation_rate=0.1):
    population = [random_state() for _ in range(pop_size)]
    for _ in range(generations):
        population.sort(key=conflicts)
        if conflicts(population[0]) == 0:
            return population[0]
        next_gen = population[:pop_size//2]
        while len(next_gen) < pop_size:
            p1, p2 = random.sample(population[:pop_size//2], 2)
            cut = random.randint(1, N-2)
            child = p1[:cut] + p2[cut:]
            if random.random() < mutation_rate:
                child[random.randint(0, N-1)] = random.randint(0, N-1)
            next_gen.append(child)
        population = next_gen
    return min(population, key=conflicts)

# --- Testcase ---
if __name__ == "__main__":
    solution = genetic()
    print("Genetic Algorithm Solution:", solution)
    print("Conflicts:", conflicts(solution))
