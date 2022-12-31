import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# POLYNOMIAL REGRESSION
# if the data points clearly will not fit a linear regression (a straight line through all data points),
# it might be ideal for polynomial regression. 
 
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# numpy mthod to make a polymonial model
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# specifying how the line will display, starting at position 1 m and end at position 22
myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()

# RELATIONSHIP COEFFICIENT (-1 to 1)
# the relationship between x and y - the coefficient of correlation - is called r
# the closer calue to 0 means there is no relationship 
relationship = r2_score(y, mymodel(x))
print(f"Relationship Coefficient = {relationship}")

# PRREDICTING FUTURE VALUE
# now we can use the information we have gathered to predict the future values.
# predicting the speed of a 10 year old car. 
speed = mymodel(22)
print(f"Predicted Speeds for 10 year old car = {speed}")
