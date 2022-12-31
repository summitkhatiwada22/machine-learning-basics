import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# MEAN
# mean = the average value
x = numpy.mean(speed)
print(f"Mean = {x}")


# MEDIAN
# median = the mid point value
y = numpy.median(speed)
print(f"Median = {y}")


# MODE
# mode = the most common value
# import stats from scipy to compute mode
z = stats.mode(speed)
print(f"Mode = {z}")





