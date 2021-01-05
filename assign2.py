import numpy as np

#Question:1
#Convert a 1D array to a 2D array with 2 rows?
arr = np.array([0,1,2,3,4,5,6,7,8,9])
arr_2d = np.reshape(arr, (2, 5))
print(arr_2d)

#Question:2
#How to stack two arrays vertically?
arr2=np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
print(np.vstack((arr_2d,arr2)))

#Question:3
#How to stack two arrays horizontally?
print(np.hstack((arr_2d,arr2)))

#Question:4
#How to convert an array of arrays into a flat 1d array?
arr_1d = arr_2d.flatten()
print(arr_1d)

#Question:5
#How to Convert higher dimension into one dimension
print(arr_2d.reshape((10,)))

#Question:6
#Convert one dimension to higher dimension
arr3=np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
arr_3=np.reshape(arr3,(5,3))
print(arr_3)

#Question:7
#Create 5x5 an array and find the square of an array
arr4=np.arange(25).reshape(5,5)
print(arr4)
print(np.square(arr4))

#Question:8
#Create 5x6 an array and find the mean
arr5=np.arange(30).reshape(5,6 )
print(np.mean(arr5))


#Find the transpose of the previous array 
arr1_transpose = arr5.transpose()
print(f'Transposed Array:\n{arr1_transpose}')


#Create a 4x4 an array and find the sum of diagonal elements
n_array = np.array([[55, 25, 15, 21], 
                    [30, 44, 2, 4], 
                    [11, 45, 77, 99]
                    [20, 22, 24, 30]]) 
  
# Displaying the Matrix 
print("Numpy Matrix is:") 
print(n_array) 
# calculating the Trace of a matrix 
trace = np.trace(n_array) 
print("\nTrace of given 3X3 matrix:") 
print(trace) 

#Find the determinant of the previous array
print(np.linalg.det(trace))
