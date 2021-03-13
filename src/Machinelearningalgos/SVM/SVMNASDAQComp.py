import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.metrics import classification_report

def mda(y_true, y_pred):
    return np.mean((np.sign(y_true[1:]-y_true[:-1]) == np.sign(y_pred[1:]-y_pred[:-1])).astype(int))
    
data = pd.read_csv("Sentiment-Categories.csv", date_parser = True)


trainingData = data[data["DateTime"]<"2021-02-18 9:30:11"].copy()
testingData = data[data["DateTime"]>="2021-02-18 9:30:11"].copy()
    

X = np.array(trainingData.drop(["MovemCatSP","DateTime","MovemCatDJIA","MovemCatNAS"], axis = 1).values.tolist())
y = np.array(trainingData["MovemCatNAS"].values.tolist())

classifier = SVC(kernel="linear")

classifier.fit(X, y)

X_test = np.array(testingData.drop(["MovemCatSP","DateTime","MovemCatDJIA","MovemCatNAS"], axis = 1).values.tolist())
y_test = np.array(testingData["MovemCatNAS"].values.tolist())

yPred = classifier.predict(X_test)

print(mda(y_test, yPred))

