import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# scipy runs on the basis of numpy and it already contains numpy libraries
# used to solve complex equations for differentiation and integration
# Used to optimize problems or programs
'''we can find the minimum value of a function
for eg :minimize f(x) = (x-3)^2'''

from scipy.optimize import minimize 

def f(x):
    return -( (x-3)**2)

res = minimize(f , 0)
print(res)


# this returns the answer as we take 0th elemnt of an array
               # res.x[0] is the minimum value of the function
