import numpy as np

# Input coefficients and constants
a1, b1, c1, d1 = map(float, input("Eq1 (a1 b1 c1 d1): ").split())
a2, b2, c2, d2 = map(float, input("Eq2 (a2 b2 c2 d2): ").split())
a3, b3, c3, d3 = map(float, input("Eq3 (a3 b3 c3 d3): ").split())

A = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
B = np.array([d1, d2, d3])

# Check if the determinant is zero
D = np.linalg.det(A)
if D == 0:
    print("No unique solution.")
else:
    # Cramer's Rule
    x = np.linalg.det(np.column_stack([B, A[:, 1], A[:, 2]])) / D
    y = np.linalg.det(np.column_stack([A[:, 0], B, A[:, 2]])) / D
    z = np.linalg.det(np.column_stack([A[:, :2], B])) / D

    print(f"\nx = {x:.3f}\ny = {y:.3f}\nz = {z:.3f}")
