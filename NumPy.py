# System in python to deal with arrays which is fast and efficient

import numpy as np
import matplotlib.pyplot as plt 

a1 = ([1,2,3,4]) # here we created an array which contains a list
a2 = np.zeros(10) # here we created an array which contains 10 elements which all are 0
                  # the number can be anything of your choice
a3  = np.random.random(10)# this gives array of 10 random numbers which are uniformly random between 0 and 1
a4 = np.random.randn(10)# this gives an array of gaussian distribution with standard deviation of 1 and mean 0
a5 = np.linspace(0,10,100)# this creates an array which goes from 0 to 10 from 100 elements which are
                          # equaly spaced apart           
a6 = np.arange(0,10,0.02)# it does the same work as linspace but here you specify the spacing required
                         # which is 0.02   
'''The arrays discussed above are the most important and frequently used'''
# the arrays in numpy are very useful as we can do any operation on these and it will do it element wise
# arrays in numpy can create boolean arrays over the condition applied to them
'''for Eg:
a1 = ([2,3,4,5)]
print(a1>4)
output = array([False,False,False,True)]
'''
# we need to plot graphs in scientific calculations

x = np.linspace(0,1,100)
plt.plot(x,x**2) #where x**2 is y
plt.show()
# we can plot histograms by 
plt.hist(a3)
plt.show()
'''The basics are done here'''