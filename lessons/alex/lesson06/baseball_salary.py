from __future__ import division
import numpy as np
from numpy import log, exp, mean
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, feature_selection


logm = linear_model.LogisticRegression()

def score(input, response):
  logm.fit(input, response)
  score = logm.score(input, salary)
  print 'R^2 Score : %.03f' % (score)

baseball = pd.read_csv('baseball.csv')
#baseball = baseball[['birthYear','bithMonth','birthDay','weight','height' ]]
baseball = baseball[['HR', 'RBI', 'R', 'G', 'SB', 'salary', 'height', 'weight', 'yearID']]
baseball = baseball.dropna()
salary = baseball['salary'].values
input = baseball[['HR', 'RBI', 'R', 'G', 'SB', 'height', 'weight', 'yearID']].values

score(input, salary)

fp_value = feature_selection.univariate_selection.f_regression(input, response)






