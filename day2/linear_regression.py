import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X = np.array([[6], [8], [10], [12], [14]])
Y = np.array([30, 40, 50, 55, 65])

model = LinearRegression()
model.fit(X,Y)

print("Slope:", model.coef_)
print("Intercept", model.intercept_)

print("Predicted price for 1100 sqft:", model.predict([[11]]))

plt.scatter(X, Y, color='blue', label='Actual data')
plt.plot(X, model.predict(X), color='red', label='Regression line')
plt.xlabel("House Size")
plt.ylabel("Price in Lakhs")
plt.title("Linear Regression")
plt.legend()
plt.show()