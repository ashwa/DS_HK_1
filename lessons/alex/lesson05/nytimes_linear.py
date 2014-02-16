import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean	
from numpy import log

nytimes = pd.read_csv('nytimes_aggregation.csv')
plt.scatter(nytimes['Age'], nytimes['CTR'])
plt.hist(nytimes['Age'], bins=range(0, 10000, 100))
plt.hist(nytimes['CTR'], bins=range(0, 10000, 100))


nytimes['log_Age'] = log(nytimes['Age'])
nytimes['log_CTR'] = log(nytimes['CTR'])
plt.scatter(nytimes['log_Age'], nytimes['log_CTR'])

from sklearn import linear_model
# Make the model object
regr = linear_model.LinearRegression()
# Fit the data
Age = [[x] for x in nytimes['Age'].values]
CTR = nytimes['CTR'].values
regr.fit(Age, CTR)

# Make the model object
log_regr = linear_model.LinearRegression()
# Fit the data
Age1 = [[x] for x in nytimes['log_Age'].values]
CTR1 = nytimes['log_CTR'].values
log_regr.fit(Age1, CTR1)

plt.scatter(Age, CTR)
#plt.plot(body, regr.predict(body), color='blue', linewidth=3, exp(body1), exp(log_regr.predict(body1), color='red', linewidth=3))
#plt.show()

# Display the coefficients:
regr.coef_
# Display our SSE:
mean((regr.predict(Age) - CTR) ** 2)
# Scoring our model (closer to 1 is better!)
ageCTR = regr.score(Age, CTR)
print ageCTR

# Display the coefficients:
regr.coef_
# Display our SSE:
mean((log_regr.predict(Age1) - CTR1) ** 2)
# Scoring our model (closer to 1 is better!)
log_ageCTR = log_regr.score(Age1, CTR1)
print log_ageCTR