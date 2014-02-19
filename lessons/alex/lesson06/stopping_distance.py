import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
cars = pd.read_csv('cars1920.csv')
#cars._get_numeric_data()
lm = linear_model.LinearRegression()
log_lm = linear_model.LinearRegression()
cars = [ [x] for x in cars['speed'].values]
log_cars = log_cars = [ [x] for x in np.log(cars['speed'].values)]
dist = cars['dist'].values
log_dist = np.log(cars['dist'].values)
lm.fit(speed, dist)
log_lm.fit(log_speed, log_dist)

lm.intercept_
log_lm.intercept_

lm.coef_
log_lm.coef_

lm.predict(speed)
cars['predict'] = lm.predict(speed)
log_lm.predict(log_speed)
cars['log_predict'] = np.exp(log_lm.predict(log_speed))

cars = cars.sort('dist')
cars_log_sort = cars.sort('log_predict')

plt.scatter(speed, dist)
plt.plot(speed, regr.predict(speed), exp(log_speed), exp(log_regr.predict(log_speed)), color='red')
plt.show()