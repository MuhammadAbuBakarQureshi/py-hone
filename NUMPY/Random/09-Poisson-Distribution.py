from numpy import random

'''
Poisson Distribution is a Discrete Distribution.

It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will 
eat thrice?

It has two parameters:

lam - rate or known number of occurrences e.g. 2 for above problem.

size - The shape of the returned array.
'''

x = random.poisson(lam = 2, size = 10)

print("\nPoisson Distribution\n", x)



'''             Visual Represantation of Poisson Distribution
'''

import seaborn as sns

import matplotlib.pyplot as plt

sns.distplot(random.poisson(lam = 2, size = 10), hist = False)

plt.show()




'''         Poisson Distribution will become similar to normal distribution with certain std dev and mean.
'''

sns.distplot(random.normal(loc = 50, scale = 7, size = 1000), hist = False)

sns.distplot(random.poisson(lam = 50, size = 1000), hist = False)

plt.show()




'''
Binomial distribution only has two possible outcomes, whereas poisson distribution can have unlimited possible outcomes.

But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is 
nearly equal to lam.

'''

sns.distplot(random.binomial(n = 1000, p = 0.01, size = 1000), hist = False)

sns.distplot(random.poisson(lam = 10, size = 1000), hist = False)

plt.show()