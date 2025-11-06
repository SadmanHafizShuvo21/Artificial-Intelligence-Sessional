import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Sample dataset
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
y = np.array([3, 6, 8, 11, 18, 25, 36, 48, 65])  # Non-linear relation

# Transform features to polynomial features (degree = 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Fit Polynomial Regression
model = LinearRegression()
model.fit(X_poly, y)

# Predict values
X_range = np.linspace(1, 9, 100).reshape(-1, 1)
y_pred = model.predict(poly.transform(X_range))

# Plot
plt.scatter(X, y, color="red", label="Data Points")
plt.plot(X_range, y_pred, color="blue", label="Polynomial Fit (degree=2)")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
