import numpy
import matplotlib.pyplot as plt

# to measure R-squared
from sklearn.metrics import r2_score

# MACHINE LEARNING TRAIN/TEST
# in ML we create models to predict the outcome of certain events.
# to measure if the model is good enough, we can use a method called Train/Test

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()

# the x axis represents the number of minutes before making a purchase.
# the y axis represents the amount of money spent on the purchase.

# the training set should be a random selection of 80% of the original data.
# the testing set should be the remaining 20%.
train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

# displaying same scatter plot with training set (80% of dandom data points)
plt.scatter(train_x, train_y)
plt.show()

# displaying same scatter plot with testing set (20% of dandom data points)
plt.scatter(test_x, test_y)
plt.show()

# the best way to visualize how the data set look like is a polynomial regression
# drawing a polynomial regression
mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()


# MEASURING R-SQUARED, R2 FOR RELIABILITY : SCORE 0 to 1
# it measures the relationship between x axis and y axis

# R2 for training
r2_training = r2_score(train_y, mymodel(train_x))
print(f'R2 Training = {r2_training}')

# R2 for testing
r2_testing = r2_score(test_y, mymodel(test_x))
print(f'R2 Testing = {r2_testing}')


# PREDICTING VALUES
# we have established that our model is acceptable at this point
# now predicting how much money will a buying customer spend if they stay in the sop for 5 minutes
five_min_spend = mymodel(5)
print(f"5 mins in store customer may spend {five_min_spend}")