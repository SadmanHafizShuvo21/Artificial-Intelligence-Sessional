# 14. SIMPSON'S 1/3 RULE
def simpson_13(f, a, b, n=100):
    if n % 2 == 1:  # make n even
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n, 2):
        s += 4 * f(a + i*h)
    for i in range(2, n, 2):
        s += 2 * f(a + i*h)
    return s * h / 3

# Example usage
result = simpson_13(lambda x: x**2, 0, 1)
print("Integral:", result)
