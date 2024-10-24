from numpy import random

'''

Logistic Distribution is used to describe growth.

Used extensively in machine learning in logistic regression, neural networks etc.

It has three parameters:

loc - mean, where the peak is. Default 0.

scale - standard deviation, the flatness of distribution. Default 1.

size - The shape of the returned array.

'''

x = random.logistic(loc = 1, scale = 2, size = (2, 3))

print("\nLogistic Distribution\n", x)



'''                 Visual Representation of Logistic Distribution
'''

import seaborn as sns

import matplotlib.pyplot as plt

sns.displot(random.logistic(loc = 1, scale = 2, size = 10))

plt.show()