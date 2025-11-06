import matplotlib.pyplot as plt
import numpy as np

def euler(f, x0, y0, x_end, h):
    x_vals = np.arange(x0, x_end, h)
    y_vals = [y0]
    for x in x_vals[:-1]:
        y_vals.append(y_vals[-1] + h * f(x, y_vals[-1]))
    return x_vals, np.array(y_vals)

# Example differential equation: dy/dx = x + y
def f(x, y):
    return x + y

# Parameters
x0, y0, x_end, h = 0, 1, 2, 0.1

# Solve and plot
x_vals, y_vals = euler(f, x0, y0, x_end, h)
plt.plot(x_vals, y_vals, label="Euler's Method")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
