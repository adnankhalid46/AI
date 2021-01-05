
import numpy as np
#Null vector of size 10 
x1=np.empty(10)
print(x1)

#Vector with values from 10  to 49
x2=np.arange(10,50,1)
print(x2)

#Find the shape of previous array in question 3
print(x2.shape)

#Print the type of the previous array in question 3
print(x2.dtype)

#Print the dimension of the array in question 3
print(x2.ndim)

#Create a boolean array with all the True values
x3=np.array((x2>9))
print(x3)

#Create a two dimensional array
x4=np.ones((5,5))
print(x4)

#Create a three dimensional array
x5=np.ones((2,5,5))
print(x5)

#Reverse a vector (first element becomes last)
x6=np.(x2)
print(x6)

#Create a null vector of size 10 but the fifth value which is 1
x7 = np.zeros(10)
print(x7)
print("Update fifth value to 1")
x7[5] = 1
print(x7)


#Create a 3x3 identity matrix
x8=np.identity(3)
print('3x3 matrix:')
print(x8)


#Convert the data type of the given array from int to float
x9= np.array([12, 10, 12])
print("Original array elements:")
print(x9)
print("Convert float values to integer values:")
print(x9.astype(float))

#Multiply arr1 with arr2
arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])  
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
mul=arr1*arr2
print(mul)

#Make an array by comparing both the arrays provided above
comp=np.maximum(arr1,arr2)
print(comp)

#Extract all odd numbers from arr with values(0-9)
x10 = np.array([1,2,3,4,5,6,7,8,9])
x11=x10[x10 % 2 == 1]
print(x11)

#Replace all odd numbers to -1 from previous array
x12=[x11-1]
print(x12)

#Replace the values of indexes 5,6,7 and 8 to 12
arr = np.arange(10)
arr[5:9]=12
print(arr)


#Create a 2d array with 1 on the border and 0 inside
x13 = np.ones((5,5))
print("Original array:")
print(x13)
print("1 on the border and 0 inside in the array")
x13[1:-1,1:-1] = 0
print(x13)

#Replace the value 5 to 12
arr2d = np.array([[1, 2,3],[4, 5, 6], [7, 8, 9]])
print(arr2d)
arr2d=replace(arr2d, arr2d==5, 12)
arr2s=[arr2d==5] <- 12
print(arr2d.shape)

#Convert all the values of 1st array to 64
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d.ndim)
arr3d[0,0,:]=64
print(arr3d)

#Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it
ar2d=np.array([[0,1,2,3,4],[5,6,7,8,9,]])
print(ar2d[1])

#Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it
print(ar2d[1,1])

#Create a 10x10 array with random values and find the minimum and maximum values
xx = np.random.random((10,10))
print("Original Array:")
print(xx) 
xxmin, xxmax = xx.min(), xx.max()
print("Minimum and Maximum Values:")
print(xxmin, xxmax)

#Find the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(a, b))

#Find the positions where elements of a and b match
a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
for i in a & b:
    if a[i]==b[i]:
        print(i)