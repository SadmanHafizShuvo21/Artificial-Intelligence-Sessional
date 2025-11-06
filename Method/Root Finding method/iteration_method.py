# 1. ITERATION METHOD
import math
def iteration_method(g, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol: 
            return x_new
        x = x_new
    return x

print(iteration_method(math.cos, 0))