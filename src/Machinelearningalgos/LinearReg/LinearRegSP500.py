import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

def mda(y_true, y_pred):
    return np.mean((np.sign(y_true[1:]-y_true[:-1]) == np.sign(y_pred[1:]-y_pred[:-1])).astype(int))

data = pd.read_csv("Sentiment-Price.csv", date_parser = True)


trainingData = data[data["DateTime"]<"2021-03-01 10:00:09"].copy()
testingData = data[data["DateTime"]>="2021-03-01 10:00:09"].copy()
    

X = np.array(trainingData.drop(["S&P500Change","DateTime","NASDAQChange","DJIAChange"], axis = 1).values.tolist())
y = np.array(trainingData.drop(["Tone", "DateTime","NASDAQChange","DJIAChange"], axis = 1).values.tolist())

regression = LinearRegression().fit(X,y)

X_test = np.array(testingData.drop(["S&P500Change","DateTime","NASDAQChange","DJIAChange"], axis = 1).values.tolist())
y_test = np.array(testingData.drop(["Tone", "DateTime","NASDAQChange","DJIAChange"], axis = 1).values.tolist())

yPred = regression.predict(X_test)

print(mda(y_test, yPred))

#Multiplied by 25 to make the trend more easily visible
plt.figure(figsize=(14,5))
plt.plot(y_test, color = 'red', label = 'Real Change')
plt.plot(yPred*25, color = 'blue', linestyle = "dashed", label = 'Predicted Change')
plt.title('Linear Regression S&P500 Change Prediction')
plt.xlabel('Time')
plt.ylabel('S&P500 Change')
plt.legend()
plt.show()