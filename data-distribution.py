import numpy
import matplotlib.pyplot as plt

# GENERATING RANDOM DATA
# creating an array containing 250 random floats between 0 and 5
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)


# HISTOGRAM
# to visualize the data set we can draw a histogram with the data we collected.
# we will use the Python module Matplotlib to draw a histogram.
plt.hist(x,5)
# we use the array to draw a histogram with 5 bars.
# the first bar represents how many values in the array are between 0 and 1.
plt.show()


# BIG DATA DISTRIBUTION
# an array containing 250 values is not considered very big, so lets plot with a bigger data set.
y = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()