# 13. TRAPEZOIDAL RULE
def trapezoidal(f, a, b, n=100):
    h = (b - a) / n
    return h/2 * (f(a) + 2*sum(f(a + i*h) for i in range(1, n)) + f(b))

# Example usage
result = trapezoidal(lambda x: x**2, 0, 1)
print("Integral:", result)
