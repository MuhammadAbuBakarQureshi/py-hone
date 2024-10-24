# Importing math module

import math


# To check all function from the module

print(dir(math))

'''
To import all Functions from the module we use asterisk

from math import *
'''




'''
You can import just one function from module

from math import sqrt

'''



num = input("Enter the number : ")

num = int(num)


# using function from module

print(math.sqrt(num))



# Using function When you have just imported that function only

# print(sqrt(num))
