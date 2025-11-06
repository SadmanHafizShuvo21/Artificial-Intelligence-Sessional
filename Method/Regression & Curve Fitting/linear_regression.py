import numpy as np

X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Calculate slope (m) and intercept (b) using least squares
m, b = np.polyfit(X, y, 1)

print("Slope:", m)
print("Intercept:", b)
print("Predicted y:", m * X + b)
