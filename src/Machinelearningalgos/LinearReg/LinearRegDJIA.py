import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

def mda(y_true, y_pred):
    return np.mean((np.sign(y_true[1:]-y_true[:-1]) == np.sign(y_pred[1:]-y_pred[:-1])).astype(int))

data = pd.read_csv("Sentiment-Price.csv", date_parser = True)


trainingData = data[data["DateTime"]<"2021-02-18 9:30:11"].copy()
testingData = data[data["DateTime"]>="2021-02-18 9:30:11"].copy()
    

X = np.array(trainingData.drop(["DJIAChange", "DateTime","NASDAQChange","S&P500Change"], axis = 1).values.tolist())
y = np.array(trainingData.drop(["Tone", "DateTime","NASDAQChange","S&P500Change"], axis = 1).values.tolist())

regression = LinearRegression().fit(X,y)

X_test = np.array(testingData.drop(["DJIAChange", "DateTime","NASDAQChange","S&P500Change"], axis = 1).values.tolist())
y_test = np.array(testingData.drop(["Tone", "DateTime","NASDAQChange","S&P500Change"], axis = 1).values.tolist())

yPred = regression.predict(X_test)

print(mda(y_test, yPred))

plt.figure(figsize=(14,5))
plt.plot(y_test, color = 'red', label = 'Real Change')
plt.plot(25*yPred, color = 'blue', linestyle = "dashed", label = 'Predicted Change')
plt.title('Linear Regression DJIA Change Prediction')
plt.xlabel('Time')
plt.ylabel('DJIA Change')
plt.legend()
plt.show()