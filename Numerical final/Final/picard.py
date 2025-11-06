import matplotlib.pyplot as plt
import numpy as np

def picards_method(f, x0, y0, x_end, h, max_iter=5):
    x_vals = np.arange(x0, x_end + h, h)
    y_vals = np.zeros((max_iter, len(x_vals)))
    
    # Initial guess (y0 at each x)
    y_vals[0, :] = y0
    
    # Iteratively apply Picard's method
    for n in range(1, max_iter):
        for i, x in enumerate(x_vals):
            integral = 0
            # Integral approximation using trapezoidal rule
            for j in range(i):
                integral += h * f(x_vals[j], y_vals[n-1, j])
            y_vals[n, i] = y0 + integral
    
    return x_vals, y_vals[-1, :]

# Example differential equation: dy/dx = x + y
def f(x, y):
    return x + y

# Parameters
x0, y0, x_end, h = 0, 1, 2, 0.1

# Solve and plot using Picard's Method
x_vals, y_vals = picards_method(f, x0, y0, x_end, h)
plt.plot(x_vals, y_vals, label="Picard's Method")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
