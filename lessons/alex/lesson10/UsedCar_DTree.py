from sklearn import datasets, metrics, tree, cross_validation
from matplotlib import pyplot as plt

usedcars = pd.read_csv('lemon_training')
usedcars = usedcars[['HR', 'RBI', 'R', 'G', 'SB', 'salary', 'height', 'weight', 'yearID']]