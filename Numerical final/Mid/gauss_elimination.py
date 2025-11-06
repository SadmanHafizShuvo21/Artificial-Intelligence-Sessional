import numpy as np
# 3x3 system: a1x + b1y + c1z = d1, etc.
print("Enter coefficients and constants for 3 equations:")
a1, b1, c1, d1 = map(float, input("Eq1 (a1 b1 c1 d1): ").split())
a2, b2, c2, d2 = map(float, input("Eq2 (a2 b2 c2 d2): ").split())
a3, b3, c3, d3 = map(float, input("Eq3 (a3 b3 c3 d3): ").split())
# Augmented matrix
aug = np.array([[a1, b1, c1, d1],
                [a2, b2, c2, d2],
                [a3, b3, c3, d3]], dtype=float)
n = 3
# Forward elimination
for i in range(n):
    for j in range(i+1, n):
        factor = aug[j, i] / aug[i, i]
        aug[j] = aug[j] - factor * aug[i]
# Back substitution
x = np.zeros(n)
x[n-1] = aug[n-1, 3] / aug[n-1, n-1]

for i in range(n-2, -1, -1):
    x[i] = (aug[i, 3] - np.sum(aug[i, i+1:n]*x[i+1:n])) / aug[i, i]

print(f"\nx = {x[0]:.3f}, y = {x[1]:.3f}, z = {x[2]:.3f}")
