import matplotlib.pyplot as plt
import numpy as np

def interpolation_method(x_values, y_values, x):
    n = len(x_values)
    result = y_values[0]
    
    for i in range(1, n):
        term = y_values[i]
        for j in range(i):
            term *= (x - x_values[j])
        result += term
        
    return result

# Example usage
x_vals = [1, 2, 3]
y_vals = [1, 4, 9]
x = 2.5

# Get the interpolated value
interpolated_value = interpolation_method(x_vals, y_vals, x)
print("Interpolated value at x =", x, "is", interpolated_value)

# Plotting the data points and the interpolation curve
x_range = np.linspace(min(x_vals) - 1, max(x_vals) + 1, 500)
y_range = [interpolation_method(x_vals, y_vals, xi) for xi in x_range]

plt.plot(x_vals, y_vals, 'ro', label='Data Points')  # Original Data Points
plt.plot(x_range, y_range, label='Interpolation Method Curve')
plt.scatter(x, interpolated_value, color='blue', zorder=5, label=f'Interpolated Value at x={x}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interpolation Method')
plt.grid(True)
plt.show()
