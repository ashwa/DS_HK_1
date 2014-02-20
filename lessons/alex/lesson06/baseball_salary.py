import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import feature_selection


logm = linear_model.LogisticRegression()

def score(input, response):
  logm.fit(input, response)
  score = logm.score(input, good)
  print 'R^2 Score : %.03f' % (score)

baseball = pd.read_csv('baseball.csv')
#baseball = baseball[['birthYear','bithMonth','birthDay','weight','height' ]]
input = baseball[['HR', 'RBI', 'R', 'G', 'SB', 'height', 'weight', 'yearID']].values
baseball = baseball.dropna()

input = baseball[ ["HR", "RBI", 'R', "G", "SB", 'height', 'weight', 'yearID'] ].values
response = baseball[['salary']].values

score(input, response)

fp_value = feature_selection.univariate_selection.f_regression(input, response)






