# 2. BISECTION METHOD
def f(x) : 
    return x**3 - x - 2

def bisection(a, b, tol=1e-6):
    if f(a) * f(b) >= 0: 
        return None
    
    while (b - a) > tol:
        c = (a + b) / 2
        if f(c) == 0: 
            return c
        elif f(a) * f(c) < 0: 
            b = c
        else: 
            a = c
    return (a + b) / 2
print(bisection(1, 2))