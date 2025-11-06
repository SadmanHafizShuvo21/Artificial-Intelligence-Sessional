import math
import numpy as np
import matplotlib.pyplot as plt

# Function definition
def f(x):
    return 5*x + 10 - 60*np.exp(-0.1*x)

# Derivative of the function
def fp(x):
    return 5 + 6*np.exp(-0.1*x)

# Newton's Method
def newton(x):
    iterations = []
    for i in range(20):
        x_new = x - f(x) / fp(x)
        iterations.append(x_new)
        if abs(x_new - x) < 1e-6:
            return x_new, iterations
        x = x_new
    return x, iterations

# Finding the root using Newton's Method
root, iterations = newton(5)

print("\nRoot =", root)

# Plotting the function and the iterations of Newton's Method
x_vals = np.linspace(0, 10, 400)
y_vals = f(x_vals)

# Plotting f(x)
plt.plot(x_vals, y_vals, label="f(x) = 5x + 10 - 60e^(-0.1x))", color='blue')
plt.axhline(0, color='black',linewidth=0.7)  # x-axis
plt.axvline(0, color='black',linewidth=0.7)  # y-axis

# Plot the iterations as red dots on the curve
iterations = np.array(iterations)
plt.plot(iterations, f(iterations), 'ro', label="Newton's Method Iterations")

plt.title("Newton's Method Convergence")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
