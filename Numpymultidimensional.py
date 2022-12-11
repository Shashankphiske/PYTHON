# 2d array (matrix)

import numpy as np

a1  = np.array([[1,2,3],[2,3,4],[3,4,5]])
print(a1)

a2 = np.random.randn(3,3)
print(a2)

# matrix operations

'''
system of equations is:
1)3x + 2y +z = 4
2)5x - 5y +4z = 3
6x + z = 0'''
A = np.array([[3,2,1],[5,-5,4],[6,0,1]])
print(A)
B = np.array([1,2,3])# we created two vectors B,C
C = np.array([-1,2,-5])

print(A@B)# we are saying multiply A matrix by B vector
          # matrix multiplied by a vector is vector
print(A.T)# transpose of the matrix

print(np.dot(B,C))# dot product of vectors
print(np.cross(B,C))# cross product of vectors
                    # cross product of vector is another vector

D = np.array([4,3,0])# vector of constants from the equation given
print(np.linalg.solve(A,D))                    
