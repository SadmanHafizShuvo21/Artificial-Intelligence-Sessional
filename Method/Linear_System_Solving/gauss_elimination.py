# def gauss_elimination(A, b):
#     n = len(A)
#     # Forward elimination
#     for i in range(n):
#         for j in range(i+1, n):
#             factor = A[j][i] / A[i][i]
#             for k in range(i, n):
#                 A[j][k] -= factor * A[i][k]
#             b[j] -= factor * b[i]
#     # Back substitution
#     x = [0] * n
#     for i in reversed(range(n)):
#         x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]
#     return x

# # Example usage
# A = [[2, 1, -1], [4, 1, 0], [-2, 3, 1]]
# b = [8, 13, 3]
# print(gauss_elimination(A, b))
def guass_elimination(a, b) :
    n = len(a)
    for i in range(n) :
        for j in range(i + 1, n) :
            fact = a[j][i] / a[i][i]
            for k in range(i, n) :
                a[j][k] -= fact * a[i][k]
            b[j] -= fact * b[i]

    # Backtracking
    x = n * [0]
    for i in reversed(range(n)) :
        x[i] = (b[i] - sum(a[i][j] * x[j] for j in range(i + 1, n))) / a[i][i]
    return x 

a = [[2, 1, -1], [4, 1, 0], [-2, 3, 1]]
b = [8, 13, 3]
result = guass_elimination(a, b) 
print(result)