import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io
import random
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

data = pd.read_csv('A_Z Handwritten Data.csv')
columns = data.columns
y = data['0']
X = data[columns[1:]]
np.shape(X) , np.shape(y)
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.999 , shuffle = True)

clf = svm.SVC(gamma = 0.01)
clf.fit(X_train,y_train)
prediction = clf.predict(X_test)
acc = metrics.r2_score(prediction , y_test)
print(f"Classification report for classifier {clf}:\n"f"{metrics.classification_report(y_test, prediction)}\n")