import numpy as np
import matplotlib.pyplot as plt

'''let y = e^-x/10 sin(x).Consider 10000x intervals in range[0,10]
1)plot the function y vs x in the range[0,10]
2)Compute the mean and standard deviation of y for x values in [4,7]
3)For x in range [4,7],find the value y^m such that 80percent of y values are less than y^m
4)Plot dy/dx vs x
5)Find the locations where dy/dx = 0'''
n = 10000
x = np.linspace(0,10,n+1) # we created the intervals

y = np.exp(-x/10)*np.sin(x) # we created the given equation

plt.plot(x,y) # we plotted the equation y with respect to x [Q1]
plt.show()

'''For [Q2] we neeed to use boolean indexing :A feature which allows filtering of values in an array'''
print(x>=4) # returns array of True or False where x satisfies condition
print(x<=7)
print(y[(x>=4)*(x<=7)])# returns all the values of y in this range on graph shown
print(np.mean(y[(x>=4)*(x<=7)]))# mean
print(np.std(y[(x>=4)*(x<=7)]))# standard deviation

'''For [Q3]'''
print(np.percentile(y[(x>=4)*(x<=7)],80)) # gives the value which greater than 80 percent of y values in 4,7

'''For [Q4]'''
plt.plot(x,np.gradient(y,x))
plt.show()

'''For [Q5]'''
dydx = np.gradient(y,x)
print(x[1:][dydx[1:] * dydx[:-1] < 0])# here we are multiplying 2 consecutive elements of dydx
# it is complicated ,but when consecutive numbers are multiplied then we can see where points are changing the 
# signs from negative to positive
# this is True when a +ve dydx point is multiplied by -ve dydx point
# thus these points are considered to be roots of the equation