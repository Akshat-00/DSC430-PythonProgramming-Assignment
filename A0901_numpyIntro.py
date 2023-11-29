# Name: Akshat Gaur
# Student ID: 2176685
# Date :11/17/2023
# I Akshat Gaur have not given or received any unauthorized assistance on this assignment.
# Youtube Link : https://youtu.be/enGy_IAaDyw

import numpy as np                          # Importing numpy

a = np.arange(0, 100, 1)                    # Creating array 'a' with 100 equally spaced values in the range 0 through 100.
print("\nArray a:\n",a)

b = np.arange(0, 100, 10)                   # Creating array 'b' with 10 equally spaced values in the range 0 through 100.
print("\nArray b:\n",b)

c = np.linspace(0, 10, 101)                 # Creating array 'c' in the range 0 through 10 (inclusive) with values spaced at 0.1.
print("\nArray c:\n",c)

d = np.random.rand(10, 10)                  # Creating a random two-dimensional array 'd' with dimensions 10 by 10.
print("\nArray d:\n",d)

a = a.reshape(10, 10)                       # Reshaping 'a' into a 10x10 array.
print("\nReshaped Array a:\n",a)

valA = a[4,5]
print("\nValue at a[4,5]:\n",valA)          # Show the value at row 4, column 5 in array 'a'.

valRowA = a[4]
print("\nValue at a[4]:\n", valRowA)        # Show the entire row 4 of array 'a'.

sumD = np.sum(d)
print("\nSum of d:\n", sumD)                # Show the sum of array 'd'.

maxA = np.max(a)
print("\nMax of a:\n", maxA)                # Show the maximum value in array 'a'.

transB = b.transpose()
print("\nTranspose of b:\n", transB)        # Show the transpose of array 'b'.

addResult = a + d
print("\nAddition -> a + d:\n", addResult)  # Show the addition of array 'a' and 'd'.

mulResult = a * d
print("\nMultiplication -> a * d:\n", mulResult)    # Show the result of multiplying 'a' and 'd'.

dotProduct = np.dot(a,d)
print("\nDot product -> a.d:\n", dotProduct)        # Show the result of computing the dot product of 'a' and 'd'.
