import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean	
from numpy import log

mammals = pd.read_csv('mammals.csv')
plt.scatter(mammals['body'], mammals['brain'])
plt.hist(mammals['body'], bins=range(0, 10000, 100))
plt.hist(mammals['brain'], bins=range(0, 10000, 100))


mammals['log_body'] = log(mammals['body'])
mammals['log_brain'] = log(mammals['brain'])
plt.scatter(mammals['log_body'], mammals['log_brain'])

from sklearn import linear_model
# Make the model object
regr = linear_model.LinearRegression()
# Fit the data
body = [[x] for x in mammals['body'].values]
brain = mammals['brain'].values
regr.fit(body, brain)

# Make the model object
log_regr = linear_model.LinearRegression()
# Fit the data
body1 = [[x] for x in mammals['log_body'].values]
brain1 = mammals['log_brain'].values
log_regr.fit(body1, brain1)

plt.scatter(body, brain)
#plt.plot(body, regr.predict(body), color='blue', linewidth=3, exp(body1), exp(log_regr.predict(body1), color='red', linewidth=3))
#plt.show()

# Display the coefficients:
regr.coef_
# Display our SSE:
mean((regr.predict(body) - brain) ** 2)
# Scoring our model (closer to 1 is better!)
parts = regr.score(body, brain)
print parts

# Display the coefficients:
regr.coef_
# Display our SSE:
mean((log_regr.predict(body1) - brain1) ** 2)
# Scoring our model (closer to 1 is better!)
log_parts = log_regr.score(body1, brain1)
print log_parts