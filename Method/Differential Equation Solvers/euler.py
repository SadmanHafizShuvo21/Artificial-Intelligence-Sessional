def euler(f, x0, y0, h, xn):
    n = int((xn - x0) / h)  # number of steps
    y = y0
    x = x0
    for _ in range(n):
        y += h * f(x, y)
        x += h
    return y

# Example: dy/dx = y, y(0)=1
result = euler(lambda x, y: y, 0, 1, 0.1, 0.5)
print("y(0.5) ≈", result)  # or use "y(0.5) ~", result if ≈ gives error
