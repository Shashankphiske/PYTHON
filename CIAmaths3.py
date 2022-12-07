# Using matrices to find solutions of equations

from sympy.interactive import printing
from sympy import Eq,solve_linear_system,Matrix
from numpy import linalg
import numpy as np
import sympy as sp
from IPython.display import display

printing.init_printing(use_latex=True)

eq1 = sp.Function('eq1')
eq2 = sp.Function('eq2')

x,y = sp.symbols('x y')
eq1 = Eq(2*x-1*y,-4)# here the equation is declared and comma takes the place of '='
# thus the equations becomes: 40x + 20y = 20
eq2 = Eq(3*x-1,-2)

row1 = [2,-1,-4]
row2 = [3,-1,-2]

system = Matrix((row1,row2))# we created a matrix of the coefficients and constants available

print(solve_linear_system(system,x,y))# the solution is being solved here for x and y
