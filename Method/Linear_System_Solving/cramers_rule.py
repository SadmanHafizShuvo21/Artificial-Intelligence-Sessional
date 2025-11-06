# 9. CRAMER'S RULE

import numpy as np
def cramers_rule(A, b):
    A = np.array(A); 
    b = np.array(b)
    detA = np.linalg.det(A)
    if abs(detA) < 1e-10: 
        return None
    n = len(b)
    x = []
    for i in range(n):
        Ai = A.copy(); 
        Ai[:, i] = b
        x.append(round(float(np.linalg.det(Ai) / detA), 10))
    return x

A = [[2,1],[5,3]]; b = [3,8]
print(cramers_rule(A, b)) 