# This is a sample project only refer to this if you want to understand how to the code in future will work

# install numpy , scipy , sympy , matplotlib
# for more info about these libraries refer to google and understand it
import scipy as sp
import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
from scipy.misc import derivative

x,a,b,c = smp.symbols('a,b,c,x' , real=True) # Here we defined our variables we are going to use 
# its always good to define this symbols and we are saying that these are real variables/values
# you can do multiple operation on these now and it will be outputed as symbolic expressions

#smp.diff(x,y,n) :this is the function used to differentiate where x is the function which we want to
#differentiate and y is the function we are differentiating it with respect to and n is the number
#how many times you need the derivative 2nd,third etc

# the derivative created can be used to derive solutions by plugging in values using 
# eg: derivativecreated.subs([x,4],[a,2],[b,3],[c,5]).evalf() it returns float value
