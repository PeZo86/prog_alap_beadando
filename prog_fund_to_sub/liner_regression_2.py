import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('files/lak0001.csv')

# Prepare the data for the linear regression model
X = data['year'].values.reshape(-1, 1)  # Independent variable (years)
y = data['dwelling'].values  # Dependent variable (dwellings)

# Initialize and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict values for the given years
predictions = model.predict(X)

# Plot the original data and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(data['year'], data['dwelling'], color='blue', label='Actual Data')
plt.plot(data['year'], predictions, color='red', label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Dwelling')
plt.title('Linear Regression of Dwelling by Year')
plt.legend()
plt.show()

# Print the model's slope and intercept
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)
