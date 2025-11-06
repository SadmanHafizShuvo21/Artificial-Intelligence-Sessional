import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2  # Example: f(x) = sin(x), you can change this

# Correct variable assignment
a = 0
b = 2
n = 10

# Calculate step size
h = (b - a) / n

# Apply Trapezoidal Rule formula
sum = f(a) + f(b)   # First and last terms

for i in range(1, n):
    x = a + i * h
    sum += 2 * f(x)   # Middle terms are multiplied by 2

# Final integration result
result = (h / 2) * sum

# Display output
print("\nApproximate value of integration = %.6f" % result)

# Optional: Plotting the function and trapezoids

x_points = [a + i*h for i in range(n+1)]
y_points = [f(x) for x in x_points]

x_fine = np.linspace(a, b, 100)
y_fine = [f(x) for x in x_fine]

plt.plot(x_fine, y_fine, 'b', label='f(x) = sin(x)')

# Draw trapezoids
for i in range(n):
    xs = [x_points[i], x_points[i], x_points[i+1], x_points[i+1]]
    ys = [0, y_points[i], y_points[i+1], 0]
    plt.fill(xs, ys, 'orange', edgecolor='red', alpha=0.3)

plt.title("Trapezoidal Rule Approximation")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()