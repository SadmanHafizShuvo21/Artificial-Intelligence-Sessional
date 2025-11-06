import matplotlib.pyplot as plt
import numpy as np

def simpsons_rule(f, a, b, n):
    # Simpson's 1/3 Rule
    if n % 2 == 1:
        n += 1  # Make sure n is even
    h = (b - a) / n
    result = f(a) + f(b)
    
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
        
    for i in range(2, n, 2):
        result += 2 * f(a + i * h)
    
    result *= h / 3
    return result

# Example function to integrate
def f(x):
    return x ** 2  # Example function (x^2)

# Example usage
a, b = 0, 2  # Interval
n = 6  # Number of subintervals (must be even)
integral_value = simpsons_rule(f, a, b, n)
print("Integral value using Simpson's 1/3 Rule is:", integral_value)

# Plotting the function and the approximation of the area
x_vals = np.linspace(a, b, 500)
y_vals = f(x_vals)

# Plot the function curve
plt.plot(x_vals, y_vals, label="f(x) = x^2", color="blue")

# Highlight the subintervals (rectangles for Simpson's Rule)
x_subintervals = np.linspace(a, b, n+1)
y_subintervals = f(x_subintervals)

# Plot the points at subintervals
plt.scatter(x_subintervals, y_subintervals, color='red', zorder=5, label='Subintervals')

# Adding annotations and title
plt.fill_between(x_vals, 0, y_vals, color="lightgray", alpha=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title("Simpson's 1/3 Rule Approximation")
plt.grid(True)
plt.show()
