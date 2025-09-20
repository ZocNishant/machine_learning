# Numerical Python (NumPy)
# Written In C

import numpy as np

# Python list
# my_list = [1, 2, 3, 4]
# print(my_list)

# numpy list
# array = np.array([1, 2, 3, 4, 5, 6])

# array *= 2

# print(array)
# print(type(array))

# Multidimentional Arrays

# multi_array = np.array("A")
# multi_array1 = np.array(["A", "B", "C"])
# multi_array2 = np.array([["A", "B", "C"], ["D", "E", "F"]])
# multi_array3 = np.array(
#     [
#         [["A", "B", "C"], ["D", "E", "F"]],
#         [["G", "H", "I"], ["J", "K", "L"]],
#         [["M", "N", "O"], ["P", "Q", "R"]],
#     ]
# )


# print(multi_array.ndim)
# print(multi_array1.ndim)
# print(multi_array2.ndim)
# print(multi_array3.ndim)
# print(multi_array3.shape)

# # shape is seen like (3,2,3) which means (layer, rows, columns)


# # chain indexing
# print(multi_array3[0][0][0])

# # multidimentional indexing
# print(multi_array3[0, 0, 0])
# print(multi_array3[0, 0, 2])


# word = multi_array3[0, 0, 0] + multi_array3[2, 1, 0] + multi_array3[1, 1, 1]
# print(word)


# Slicing

# array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# # array[start:end:step]

# print(array[2:, 2:])

# scalar arithmetic

# array = np.array([1, 2, 3])

# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array**3)
# print(array / 4)

# print(np.sqrt(array))
# print(np.pi)

# Broadcasting allows NumPy to perform operations on arrays with different shapes by virtually expanding dimensions so they match the larger array shape. The dimensions have the same size or one of the dimentions has a size of 1.

# array1 = np.array([[1, 2, 3, 4]])
# array2 = np.array([[6], [7], [8], [9]])

# print(array1.shape)
# print(array2.shape)

# print(array1 * array2)

# aggregate functions - summarize data and typically return a single value

# array = np.array([[1, 2, 4, 5, 6], [9, 8, 7, 6, 5]])

# print(np.mean(array))
# print(np.std(array))
# print(np.argmin(array))

# print(np.sum(array, axis=0))
# print(np.sum(array, axis=1))

# filtering - refers to the process of selecting elements from an array that match agiven condition

array_ages = np.array([[21, 22, 32, 14, 16], [44, 54, 35, 66, 75]])

teen = array_ages[array_ages < 18]
adults = array_ages[(array_ages >= 18) & (array_ages <= 55)]
old = array_ages[array_ages > 55]

print(teen)
print(adults)
print(old)
