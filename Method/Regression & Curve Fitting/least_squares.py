import numpy as np
import matplotlib.pyplot as plt

def least_squares_regression(x, y):
    # Calculate the sums required for the least squares formulas
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x_squared = np.sum(x ** 2)
    
    # Calculate the slope (m) and intercept (b)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = (sum_y - m * sum_x) / n
    
    return m, b

# Example data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Compute the best fit line
m, b = least_squares_regression(x, y)

# Generate the fitted line using the slope and intercept
y_fit = m * x + b

# Plot the original data and the fitted line
plt.scatter(x, y, color='red', label='Data points')
plt.plot(x, y_fit, color='blue', label=f'Fitted line: y = {m:.2f}x + {b:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title("Least Squares Regression")
plt.show()

# Output the slope and intercept
print(f"Slope (m): {m:.2f}")
print(f"Intercept (b): {b:.2f}")