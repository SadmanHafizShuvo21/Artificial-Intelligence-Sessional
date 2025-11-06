# 12. LAGRANGE INTERPOLATION
def lagrange(x_data, y_data, x):
    result = 0
    for i in range(len(x_data)):
        term = y_data[i]
        for j in range(len(x_data)):
            if j != i:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term
    return result
print(lagrange([0,1,2], [1,0,1], 1.5))