import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

# SCALE FEATURES
# when data has different values, and even different measurement units, it can be difficult to compare them. 
# what is kilograms compared to meters? Or altitude compared to time? the answer to this problem is scaling. 
# we can scale data into new values that are easier to compare.

# there are different methods for scaling data, here we will use a method called standardization.
# the standardization method uses this formula:
# z = (x - u) / s
# where z is the new value, x is the original value, u is the mean and s is the standard deviation.

# if we take the weight column from the data set above, the first value is 790, and the scaled value will be:
# (790 - 1292.23) / 238.74 = -2.1
# if we take the volume column from the data set above, the first value is 1.0, and the scaled value will be:
# (1.0 - 1.61) / 0.38 = -1.59
# now you can compare -2.1 with -1.59 instead of comparing 790 with 1.0.

# we can use Python sklearn module's method called StandardScaler() to do this

scale = StandardScaler()
df = pandas.read_csv('data.csv')
X = df[['Weight', 'Volume']]
scaledX = scale.fit_transform(X)
print(scaledX)

# PREDICTING CO2 VALUES
# predicting co2 emission from a 1.3 liter casr that weighs 2300 kilograms
y = df[['CO2']]
scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(f'Predicted CO2 = {predictedCO2}')