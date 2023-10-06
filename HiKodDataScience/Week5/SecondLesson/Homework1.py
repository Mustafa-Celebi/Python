import numpy as np
import pandas as pd
#! Finding 1D array's size and lenght

array_1 = np.array([1,2,3,4,5,6,7,8,9],dtype=int)

print(type(array_1))

a = len(array_1)
print(a)
#? 9

print(array_1.ndim)
#? 1

#! 2D Array

array_2 = np.array([[10,20,30],[50,60,70],[80,90,100]])

b = len(array_2)
print(b)
#? 3

print(array_2.ndim)
#? 2

#! 3D Array

array_3 = np.array([[[1,2],[3,4]],[[5,7],[8,9]]])

c = len(array_3)
print(c)
#? 2

print(array_3.ndim)
#? 3

#! Slicing & Indexing

print(array_1[2:6])
#? 3,4,5,6

print(array_2[0,1])
#? 20

print(array_3[1,1])
#? 8,9

print(array_1[0:-3])
#? 1,2,3,4,5,6

zero_1 = np.zeros(7)
print(zero_1)

zero_2 = np.zeros(10)
print(zero_2)

zero_3 = np.concatenate((zero_1,zero_2),axis=0)
print(zero_3)
#? [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]