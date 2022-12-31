import numpy

speed = [86,87,88,86,87,85,86]
speed_2 = [32,111,138,28,59,77,97]

# STANDAED DEVIATION
# standard deviation is a number that describes how spread out the values are.
# a low standard deviation means that most of the numbers are close to the mean (average) value.
# a high standard deviation means that the values are spread out over a wider range.

sd = numpy.std(speed)
sd_2 = numpy.std(speed_2)
print(f"Standard Deviation(SD) = {sd}")
print(f"Standard Deviation(SD) = {sd_2}")


# VARIANCE
# variance is another number that indicates how spread out the values are.
# in fact, if you take the square root of the variance, you get the standard deviation!
# or the other way around, if you multiply the standard deviation by itself, you get the variance!
variance = numpy.var(speed)
variance_2 = numpy.var(speed_2)
print(f'Variance = {variance}')
print(f'Variance = {variance_2}')






