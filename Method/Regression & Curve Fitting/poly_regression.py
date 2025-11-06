# 20. POLYNOMIAL REGRESSION
import numpy as np
def poly_regression(x, y, deg=2):
    X = np.vander(x, deg + 1, increasing=True)
    return np.linalg.lstsq(X, y, rcond=None)[0]
x = [0,1,2,3]; y = [1,2,4,8]
print(poly_regression(x, y, 2))