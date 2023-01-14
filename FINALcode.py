import scipy as sp

def f(params):
    x , y = params
    return 
first_guess = [0,0]    
res = sp.optimize.minimize(f,first_guess)
print(res)
