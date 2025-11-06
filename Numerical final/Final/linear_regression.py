import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Example data
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Reshape for a single feature
y = np.array([2, 4, 5, 4, 5])

# Initialize the LinearRegression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Get the slope (m) and intercept (b)
m = model.coef_[0]  # Slope
b = model.intercept_  # Intercept

# Generate the predicted y values
y_pred = model.predict(x)

# Plot the original data and the fitted regression line
plt.scatter(x, y, color='red', label='Data points')
plt.plot(x, y_pred, color='blue', label=f'Fitted line: y = {m:.2f}x + {b:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title("Linear Regression")
plt.show()

# Output the slope and intercept
print(f"Slope (m): {m:.2f}")
print(f"Intercept (b): {b:.2f}")
