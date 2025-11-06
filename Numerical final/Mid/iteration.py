import math

# ফাংশন নির্ধারণ
def g(x):
    return (60*math.exp(-0.1*x) - 10) / 5   # এখানে x = g(x)

def iteration(x0, tol=1e-6, max_iter=50):
    for i in range(max_iter):
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1

# প্রাথমিক অনুমান (initial guess)
root = iteration(5)
print(f"\nRoot ≈ {root:.6f}")
