# -*- coding: utf-8 -*-
"""lab exam.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JAfMvBPQCQR21CmMUAY_s6LPBWX-jJE1
"""

#importing the libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report
from sklearn.datasets import load_iris

#load the iris dataset
iris=load_iris()
X,y=iris.data,iris.target

#split into train and testing datasets
x_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#create a LogisticRegression model
model=LogisticRegression()
model.fit(x_train,y_train)

#Evaluate the model
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
report=classification_report(y_test,y_pred)
print("Accuracy_score:",accuracy)
print("classification_report:\n",report)