from numpy import random

'''
        Binomial Distribution is a Discrete Distribution


It has three parameters:

n - number of trials.

p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).

size - The shape of the returned array.(Data points)
'''


x = random.binomial(n = 10, p = 0.5, size = 10)

print("\nBinomail Distribution\n", x)


'''         Visual Representation
'''

import seaborn as sns

import matplotlib.pyplot as plt

sns.distplot(random.binomial(n = 10, p = 0.5, size = 1000), hist = False)

plt.show()



'''         Normal VS Binomial Distribution


The main difference is that Normal distribution is contiuos, where as Binomial is discrete.

If there are enough data points it will be similar to Normal distribution with certain loc and scale

'''


sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label="normal")

sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label="binomial")

plt.show()