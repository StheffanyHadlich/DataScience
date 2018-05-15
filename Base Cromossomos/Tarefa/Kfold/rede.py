from sklearn.model_selection import KFold 
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import classification_report, confusion_matrix

import pandas as pd
import numpy as np
import pickle

rede = pickle.load(open('rede.sav', 'rb'))
print(rede)
prediction = pd.read_csv('Edinburgo\\B3.csv', names = ["var1", "var2", "var3", "class"])


xTest = prediction.drop('class',axis=1)
yTest = prediction['class']
tests = rede.predict(xTest)
print(confusion_matrix(yTest,tests))
print(classification_report(yTest,tests))

from matplotlib import pyplot as plt
plt.scatter(yTest, tests)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.show()