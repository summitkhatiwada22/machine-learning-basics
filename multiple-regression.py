import pandas
from sklearn import linear_model

# MULTIPLE REGRESSION
# multiple regression is like linear regression, but with more than one independent value,
# meaning that we try to predict a value based on two or more variables. 
# eg. we can predict the CO2 emission of a car based on the size of the engine,
# but with multiple regression we can throw in more variables, like the weight of the car, to make the prediction more accurate.

df = pandas.read_csv("data.csv")

# it is common to name the list of independent values with X, and the dependent values with y
# making a list of the independent values and call this variable X
X = df[['Weight', 'Volume']]

# putting the dependent values in a variable called y
y = df['CO2']

# we use LinearRegression() from sklearn to create a linear regression object and use a method called fit()
regr = linear_model.LinearRegression()
regr.fit(X, y)

# at this point we can predict
# predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictCO2 = regr.predict([[2300, 1300]])
print(f"Prediction = {predictCO2}")  
# answer = 107.29
# We have predicted that a car with 1.3 liter engine, and a weight of 2300 kg, 
# will release approximately 107 grams of CO2 for every kilometer it drives.

# COEFFICIENT 
# the relationship between x and y - the coefficient of correlation - is called r
# the closer calue to 0 means there is no relationship 
relationship = regr.coef_
print(f"Relationship Coefficient = {relationship}")
# the result array represents the coefficient values of weight and volume.
# weight: 0.00755095
# volume: 0.00780526
# these values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.
# and if the engine size (Volume) increases by 1 cm3, the CO2 emission increases by 0.00780526 g.