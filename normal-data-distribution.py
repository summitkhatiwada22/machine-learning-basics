import numpy
import matplotlib.pyplot as plt

# NORMAL DISTRIBUTION
# how to create an array where the values are concentrated around a given value?
# in probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution.
# a normal distribution graph is also known as the bell curve.
x = numpy.random.normal(5.0, 1.0, 100000)
# mean = 5.0; sd = 1.0; number of data = 100000
plt.hist(x, 100)
plt.show()