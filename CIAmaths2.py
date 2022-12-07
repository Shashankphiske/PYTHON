# Finding solutions of equations in python

import numpy as np

eq = [1,5,6] # here the equation taken as example is x^2+5x+6 = 0
# only the coefficients are given in the list and the variable is taken as default
roots = np.roots(eq) # np.roots() is the function of numpy to find roots
print(roots)