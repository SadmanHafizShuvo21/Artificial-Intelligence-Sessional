import math
import numpy as np
import matplotlib.pyplot as plt
# Define the function to integrate
def f(x):
    return x**2  # Example: f(x) = sin(x), you can change
a , b, n = 0, 2, 10

# Check if n is multiple of 3

# Step size
h = (b - a) / n
# Apply Simpson's 3/8 Rule
sum = f(a) + f(b)
for i in range(1, n):
    x = a + i * h
    if i % 3 == 0:
        sum += 2 * f(x)  # Terms divisible by 3 multiplied by 2
    else:
        sum += 3 * f(x)  # Other terms multiplied by 3

# Final integration result
result = (3 * h / 8) * sum
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
