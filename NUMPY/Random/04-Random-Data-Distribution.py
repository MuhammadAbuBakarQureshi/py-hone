from numpy import random


'''         Generating 2-D array 

you can also generate any dimension array by using "size"
'''

x = random.choice([2, 1, 6, 5], p = [0.1, 0.2, 0.7, 0], size = (3, 5))

# The sum of all probability numbers should be 1

print("\nRandom 2-D array using Choice method\n", x)