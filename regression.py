import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import  mean_squared_error

daibetes = datasets.load_diabetes()
daibetes_X = daibetes.data[:, np.newaxis,2]

daibetes_X_train= daibetes_X[:-30]
daibetes_X_test= daibetes_X[-20:]

daibetes_Y_train= daibetes.target[:-30]
daibetes_Y_test= daibetes.target[-20:]

model= linear_model.LinearRegression()
model.fit(daibetes_X_train,daibetes_Y_train)

diabetes_y_predicted = model.predict(daibetes_X_test)

print("Mean squared error is: ", mean_squared_error(daibetes_Y_test, diabetes_y_predicted))

print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)

plt.scatter(daibetes_X_test, daibetes_Y_test)
plt.plot(daibetes_X_test, diabetes_y_predicted)

plt.show()

# print(daibetes_X)