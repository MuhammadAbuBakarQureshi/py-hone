import numpy as np


'''     Finding Data types
'''

arr = np.array([2, 4])

print(arr.dtype) # int32

arr = np.array(["Apple", "Banana"])

print(arr.dtype)




'''     Creating Arrays With a Defined Data Type
'''

arr = np.array([4, 2, 6], dtype = 'int16')

print(arr.dtype) # int16


'''We can give size as well
'''
arr = np.array([5, 2, 6], dtype = 'i8') # Data type integer and itemsize is 8 bytes

print(arr.dtype, arr.itemsize) # int32 8



'''     Get size
'''

arr = np.array([1 ,3 , 5])

''' "itemsize" gives Each Element size in the array
'''
print(arr.itemsize) # 4




''' "size" gives How many elements in the array

Float is 8 bytes
'''
print(arr.size) # 3






'''
                            Converting Data Type on Existing Arrays

                            
The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for 
float and int for integer.

'''


arr = np.array([5.2, 7.7, 3.5, 7.1, 4.3 , 6.7])

print(arr.dtype) # float64

new_arr = arr.astype(int)

print(new_arr.dtype) # int32

new_arr = new_arr.astype(bool)

print(new_arr.dtype) # bool