# 15. SIMPSON'S 3/8 RULE
def simpson_38(f, a, b, n=99):
    # Make n a multiple of 3
    if n % 3 != 0:
        n += 3 - (n % 3)
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            s += 2 * f(a + i*h)
        else:
            s += 3 * f(a + i*h)
    return s * 3 * h / 8

# Example usage
result = simpson_38(lambda x: x**2, 0, 1)
print("Integral:", result)
