import numpy as np

# 3x3 সমীকরণ
# a1x + b1y + c1z = d1
# a2x + b2y + c2z = d2
# a3x + b3y + c3z = d3
print("Enter coefficients and constants for 3 equations:")
a1, b1, c1, d1 = map(float, input("Eq1 (a1 b1 c1 d1): ").split())
a2, b2, c2, d2 = map(float, input("Eq2 (a2 b2 c2 d2): ").split())
a3, b3, c3, d3 = map(float, input("Eq3 (a3 b3 c3 d3): ").split())
# Augmented matrix তৈরি করা
aug = np.array([[a1, b1, c1, d1],
                [a2, b2, c2, d2],
                [a3, b3, c3, d3]], dtype=float)
n = 3  # number of variables
# Gauss-Jordan elimination
for i in range(n):
    # Pivot কে 1 করা
    aug[i] = aug[i] / aug[i, i]

    # অন্য সব row থেকে এই column কে 0 করা
    for j in range(n):
        if i != j:
            aug[j] = aug[j] - aug[j, i]*aug[i]

# Solution বের করা
x, y, z = aug[:, 3]
print(f"\nx = {x:.3f}, y = {y:.3f}, z = {z:.3f}")
