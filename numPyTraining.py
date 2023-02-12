#Numpy is a python library used for working with arrays
#array obj of numpy : ndarray

import numpy as np

# arr = np.array([1,2,3,4,5])
# print(arr)

#checking numpy version
# print(np.__version__)

# print(type(arr))

#0D-array (scalars)

# arr = np.array(42)
# print(arr)

#1D array is the typical array where each elements is a 0D array

#2D array is an array that has 1D arrays as its elements, they are often used to represent matrix or 2nd order tensors

# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)

#3D arrays

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)


#ndim function returns dimension of the array

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

#Numpy array indexing 
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# targetedElem = arr[0,3]

# print(f"the element value : {targetedElem}")

#Numpy array slicing （taking elements from start index to end index) syntax : [start:end:step]

# arr = np.array([1,2,3,4,5,6,7])

# print(arr[1:5])

#Slicing 2D arrays
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1,1:4])

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[0:2, 2])

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[0:2, 1:4])

#specifying data type when initializing array
# arr = np.array([1,2,3,4], dtype='S')
# print(arr)
# print(arr.dtype)
# print(type(arr[0]))

#Converting Data Type on Existing Arrays
#make a copy of the array with astype() and specifying data type as parameter
# arr = np.array([1.5,2.3,3.2])
# secArr = arr.astype('i')
# print(secArr)

#Numpy Array Shape : shape of an array is the number of elements in each dimension
# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.shape) #returns (2,4) : first dimension has 2 elements, second dimension has 4 elements

#Reshaping array
#1D to 2D
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr)

#1D to 3D
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr)

#Unknown Dimension
#we are allowed to have one unknown dimension, meaning we do x have to specify an exact number
# for one of the dimensions in the reshape method by passing -1 as the value

#e.g convert 1D array with 8 elements to 3D array with 2x2 elements
# arr = np.array([1,2,3,4,5,6,7,8])
# newarr = arr.reshape(2,2,-1)
# print(newarr)

#Flattening the arrays : converting multidimensional arrays into 1D array through reshape(-1)
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr)

#Numpy array iterating
# arr = np.array([[1,2,3],[4,5,6]])

#nested for loop depth based on dimension lvl
# for x in arr:
#     print(f"{x} is the row")
#     for y in x:
#         print(f"{y} is the element in the row" )

#iterating 3D arrays

# arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(arr.shape)

# for x in arr:
#     print(x)
#     for y in x:
#         print(y)
#         for z in y:
#             print(z)

#Iterating arrays using nditer()

#iterating each scalar element
# arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# for x in np.nditer(arr):
#   print(x)

#Numpy joining arrays

#joining two arrays, axis 0 = row, axis 1 = column ; following according to shape of array
# arr1 = np.array([[1,2,3],[10,11,12]])
# arr2 = np.array([[4,5,6],[7,8,9]])

# arr = np.concatenate((arr1,arr2),axis=1)
# print(arr)

# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.stack((arr1, arr2),axis=1)

# print(arr)

#stack along columns : vstack()
# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.vstack((arr1, arr2))

# print(arr)

#stack along rows : hstack()
# arr1 = np.array([1, 2, 3])

# arr2 = np.array([4, 5, 6])

# arr = np.hstack((arr1, arr2))

# print(arr)

# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])

# arr = np.stack((arr1, arr2), axis=1)

# print(arr)

# arr1 = np.array([[1, 2], [3, 4]])

# arr2 = np.array([[5, 6], [7, 8]])

# arr = np.dstack((arr1, arr2))

# print(arr)


#Splitting array : array_split()
# arr = np.array([1,2,3,4,5,6])
# newArr = np.array_split(arr,3)
# print(newArr)

#splitting 2D array
# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr, 3)
# print(newarr)

#Searching arrays : where() method
# arr = np.array([1,2,3,4,5,4,4])
# x = np.where(arr == 4)
# print(x)

#search sorted method which performs binary search in the array; but it assumes the array is sorted
#and it returns the index where the specified value would be inserted
# arr = np.array([6,7,8,9])
# x = np.searchsorted(arr,7)
# print(x)

#sorting arrays : sort()

# arr = np.array([2,1,3,0])
# print(np.sort(arr))

#sorting 2D array
# arr = np.array([[3,2,4],[5,0,1]])
# print(np.sort(arr))

#Filtering array is done by providing boolean index list
# arr = np.array([41,42,43,44])
# x = [True, False, True, False]
# newarr = arr[x]
# print(newarr)