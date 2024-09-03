import numpy as np
#arrray slicing :
arr = np.array([1,2,3,4,5,6,7,8])

print(arr[1:3]) #gives array in between index 1 and 3 excluding 3rd
print(arr[1:]) #ending at the array ending
print(arr[:5]) #ending excluding the 5th element
x = arr[0:7:2] #starting and ending index with a step of 2
print(x)

print(arr[-4:-1]) #excluding the -1 element
print(arr[::2]) #starting and ending same as the original array but with 2 step

print(arr.shape) #array has 1 dimension, where it has 8 elements
newarr = arr.reshape(2,4) #reshape the 1d array into 2d with 4 elements each
print(newarr) #we cannot reshape this array where we dont have elements to put in each dimension eg : cant reshape in 3d with 4 elements
