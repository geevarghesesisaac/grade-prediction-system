##importing required ml libraries
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split

##importing dataset
ds = pd.read_csv(r'D:\Mini Project\Grade Prediction\data.csv')

##selecting target class
x = ds.drop("Result",axis=1)
y = ds["Result"]

##splitting data for training and testing
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.20,random_state=0)

##svm algorithm
from sklearn import svm

sv = svm.SVC(kernel='linear')

##training
sv.fit(X_train, Y_train)

import pickle
pickle.dump(sv,open("model.pkl", "wb"))