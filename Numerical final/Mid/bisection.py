import math
import numpy as np
import matplotlib.pyplot as plt

# Function definition
def f(x):
    return 5*x + 10 - 60*math.exp(-0.1*x)

# Bisection Method with Plotting
def bisection(a, b, tol=1e-6):
    if f(a)*f(b) > 0:
        print("Invalid range! Root may not exist.")
        return None

    # Plotting the function
    x_vals = np.linspace(a, b, 400)  # Array of x values for plotting
    y_vals = 5*x_vals + 10 - 60*np.exp(-0.1*x_vals)  # Function values for the plot
    plt.plot(x_vals, y_vals, label="f(x) = 5x + 10 - 60e^(-0.1x))", color='blue')
    plt.axhline(0, color='black',linewidth=0.7)  # x-axis
    plt.axvline(0, color='black',linewidth=0.7)  # y-axis
    plt.title("Bisection Method Convergence")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    iteration_steps = []

    for i in range(50):
        c = (a + b) / 2
        iteration_steps.append(c)

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        # Highlight the current midpoint of the interval
        plt.plot(c, f(c), 'ro')  # Red dot for the current midpoint

        # Check if the tolerance condition is met
        if abs(f(c)) < tol:
            break

    plt.legend()
    plt.grid(True)
    plt.show()

    return c

# Initial values (example)
root = bisection(0, 10)
print(f"\nRoot ≈ {root:.6f}")
