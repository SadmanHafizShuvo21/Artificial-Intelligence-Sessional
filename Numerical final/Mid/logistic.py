import numpy as np
import matplotlib.pyplot as plt
def logistic_regression(x):
    return 1 / (1 + np.exp(-x))

def predict_logistic(x, m, b):
    linear_combination = m * x + b
    return logistic_regression(linear_combination)

# An example usage
predict_logistic(0, 1, 0), predict_logistic(1, 1, 0), predict_logistic(-1, 1, 0)

x = np.linspace(-10, 10, 100)
y = logistic_regression(x)
plt.plot(x, y)
plt.show()