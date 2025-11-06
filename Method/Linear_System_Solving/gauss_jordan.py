# 5. GAUSS JORDAN ELIMINATION
def gauss_jordan(A, b):
    n = len(A)
    for i in range(n):
        # Make the diagonal element 1
        factor = A[i][i]
        for j in range(n):
            A[i][j] /= factor
        b[i] /= factor

        # Make other elements in column i zero
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                b[k] -= factor * b[i]
    return b

# Example usage
A = [[2, 1, -1], [4, 1, 0], [-2, 3, 1]]
b = [8, 13, 3]
print(gauss_jordan(A, b))
