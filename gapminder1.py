# TODO: Add import statements
import pandas as pd
from sklearn import linear_model

# Assign the dataframe to this variable.
# TODO: Load the data
bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv')
x_values = bmi_life_data[['Life expectancy']]
y_values = bmi_life_data[['BMI']]


# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model
bmi_life_model = linear_model.LinearRegression()
bmi_life_model.fit(y_values, x_values)

# Mak a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
laos_life_exp = bmi_life_model.predict(21.07931)
