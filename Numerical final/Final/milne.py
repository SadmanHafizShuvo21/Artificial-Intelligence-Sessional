import matplotlib.pyplot as plt
import numpy as np

def runge_kutta(f, x0, y0, x_end, h):
    x_vals = [x0]
    y_vals = [y0]
    for x in np.arange(x0, x_end, h):
        k1 = h * f(x, y_vals[-1])
        k2 = h * f(x + h/2, y_vals[-1] + k1/2)
        k3 = h * f(x + h/2, y_vals[-1] + k2/2)
        k4 = h * f(x + h, y_vals[-1] + k3)
        y_vals.append(y_vals[-1] + (k1 + 2*k2 + 2*k3 + k4) / 6)
        x_vals.append(x + h)
    return np.array(x_vals), np.array(y_vals)

def milnes_method(f, x0, y0, x_end, h):
    # Step 1: Use Runge-Kutta to get the first 4 values
    x_vals, y_vals = runge_kutta(f, x0, y0, x0 + 3*h, h)
    # runge_kutta returns numpy arrays; convert to lists so we can append
    x_vals = list(x_vals)
    y_vals = list(y_vals)
    
    # Step 2: Use Milne's method (Predictor-Corrector)
    for x in np.arange(x0 + 3*h, x_end, h):
        # Predictor (4th-order)
        p = y_vals[-4] + (4*h / 3) * (2*f(x - 3*h, y_vals[-4]) - f(x - 2*h, y_vals[-3]) + 2*f(x - h, y_vals[-2]))
        # Corrector (3rd-order)
        y_next = y_vals[-3] + (h / 3) * (f(x - h, y_vals[-2]) + 4*f(x, p) + f(x + h, y_vals[-1]))
        y_vals.append(y_next)
        x_vals.append(x + h)
    
    return np.array(x_vals), np.array(y_vals)

# Example differential equation: dy/dx = x + y
def f(x, y):
    return x + y

# Parameters
x0, y0, x_end, h = 0, 1, 2, 0.1

# Solve and plot using Milne's Method
x_vals, y_vals = milnes_method(f, x0, y0, x_end, h)
plt.plot(x_vals, y_vals, label="Milne's Method")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
