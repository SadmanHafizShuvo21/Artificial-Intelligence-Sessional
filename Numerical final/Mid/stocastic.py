import matplotlib.pyplot as plt
import numpy as np

def stochastic_gradient_descent(x, y, m=0, b=0, learning_rate=0.01, epochs=10000):
    n = len(y)
    for _ in range(epochs):
        for i in range(n):
            xi = x[i:i+1]
            yi = y[i:i+1]
            y_pred = m * xi + b
            dm = -2 * xi * (yi - y_pred)
            db = -2 * (yi - y_pred)
            m -= learning_rate * dm
            b -= learning_rate * db
    return m, b

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

plt.scatter(x, y)

m, b = stochastic_gradient_descent(x, y)
plt.plot(x, m*x + b, color='red')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Stochastic Gradient Descent')
plt.show()


