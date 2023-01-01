import scipy as sp

def f(x):
    return -(x**3 + 3*(x**2) - 3*x + 90)
res = sp.optimize.minimize(f,0)
print(res)