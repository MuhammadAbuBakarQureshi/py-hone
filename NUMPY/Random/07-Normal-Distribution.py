import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

'''

It is also calles the Gaussian Distribution

It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
'''

x = random.normal(size=(3, 3))

print("\nNormal Distribution\n", x)

'''
It has three parameters

loc - (mean) Where the peak of the bell exits

scale - (Standard Deviation) how flat the graph distribution should be.

size - The shape of the returned array.

'''


x = random.normal(loc = 6, scale = 2, size = (3, 2))

print("\n\nNormal Distribution using loc parameter\n", x)



'''         Visual Representation of Normal Distribution
'''

sns.distplot(random.normal(loc = 6, scale= 1, size = (2, 2)), hist = False)

plt.show()