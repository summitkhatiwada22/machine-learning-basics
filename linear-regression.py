import matplotlib.pyplot as plt
from scipy import stats

# REGRESSION
# the term regression is used when you try to find the relationship between variables.
# in Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.

# LINEAR REGRESSION
# linear regression uses the relationship between the data-points to draw a straight line through all them.
# this line can be used to predict future values.

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# writing a method that returns some importrant key values of Linear Regression
slope, intercept, r, p, std_err = stats.linregress(x, y)

# a function that uses the slope and intercept values to return a new value.
# this new value represents where on the y-axis the corresponding x value will be placed.
def myfunc(x):
    return slope * x + intercept

# running each value of the x array through the function. This will result in a new array with new values for the y-axis. 
mymodel = list(map(myfunc, x))

# drawing the original scatter plot.
plt.scatter(x, y)

# drawing the line of linear regression.
plt.plot(x, mymodel)

# displaying the diagram. 
plt.show()

# RELATIONSHIP COEFFICIENT (-1 to 1)
# the relationship between x and y - the coefficient of correlation - is called r
# the closer calue to 0 means there is no relationship 
print(f"Relationship Coefficient = {r}")

# PRREDICTING FUTURE VALUE
# now we can use the information we have gathered to predict the future values.
# predicting the speed of a 10 year old car. 
speed = myfunc(10)
print(f"Predicted Speeds for 10 year old car = {speed}")

