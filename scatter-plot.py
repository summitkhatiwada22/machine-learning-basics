import numpy
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# SCATTER PLOT
# a scatter plot is a diagram where each value in the data set is represented by a dot.
# the Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length, 
# one for the values of the x-axis, and one for the values of the y-axis:
plt.scatter(x, y)
plt.show()

# RANDOM DATA DISTRIBUTION
# a scatter plot with 1000 dots
set_1 = numpy.random.normal(5.0, 1.0, 1000)
set_2 = numpy.random.normal(10.0, 2.0, 1000)
plt.scatter(set_1, set_2)
plt.show()