import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras
import tensorflow
from tensorflow.python.keras.losses import MeanSquaredError

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python import training



data = pd.read_csv("Sentiment-Price.csv", date_parser = True)


trainingData = data[data["DateTime"]<"2021-03-01 10:00:09"].copy()
testingData = data[data["DateTime"]>="2021-03-01 10:00:09"].copy()

trainingData = trainingData.drop(["DateTime","DJIAChange","S&P500Change"], axis =1)

#scaler = MinMaxScaler()

trainingData = np.array(trainingData.values.tolist())#scaler.fit_transform(trainingData)

def mda(y_true, y_pred):
    return np.mean((np.sign(y_true[1:]-y_true[:-1]) == np.sign(y_pred[1:]-y_pred[:-1])).astype(int))
    
    # c = tensorflow.equal(tensorflow.cast(tensorflow.sign(y_true[1:] - y_true[:-1]), tensorflow.float32), tensorflow.cast(tensorflow.sign(y_pred[1:] - y_pred[:-1]), tensorflow.float32))
    # return tensorflow.reduce_mean(tensorflow.cast(c, tensorflow.float32))

X_train = []
y_train = []

for i in range(3, trainingData.shape[0]):
    X_train.append(trainingData[i-3:i])
    y_train.append(trainingData[i, 0])

X_train, y_train = np.array(X_train), np.array(y_train)

regressor = Sequential()

regressor.add(LSTM(units = 50, activation = "relu", return_sequences=True, input_shape = (X_train.shape[1], 2)))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 60, activation = "relu", return_sequences=True))
regressor.add(Dropout(0.3))

regressor.add(LSTM(units = 80, activation = "relu", return_sequences=True))
regressor.add(Dropout(0.4))

regressor.add(LSTM(units = 80, activation = "relu"))
regressor.add(Dropout(0.5))

regressor.add(Dense(units =1))

#Adam is stochasitc gradient descent and I use mean squared error as the loss function
regressor.compile(optimizer="adam", loss=tensorflow.keras.losses.MSE)
regressor.fit(X_train, y_train, epochs=5, batch_size=16)


past2Days = data[data["DateTime"]<"2021-03-01 10:00:09"].copy().tail(3)

df = past2Days.append(testingData, ignore_index = True)
df = df.drop(["DateTime","DJIAChange","S&P500Change"], axis =1)

inputs = np.array(df.values.tolist())

X_test = []
y_test = []

for i in range(3, inputs.shape[0]):
    X_test.append(inputs[i-3:i])
    y_test.append(inputs[i, 0])

X_test, y_test = np.array(X_test), np.array(y_test)

yPred = regressor.predict(X_test)

print(mda(y_test, yPred))

plt.figure(figsize=(14,5))
plt.plot(y_test, color = 'red', label = 'Real Change')
plt.plot(yPred, color = 'blue',  linestyle = "dashed", label = 'Predicted Change')
plt.title('LSTM NASDAQ Composite Change Prediction')
plt.xlabel('Time')
plt.ylabel('NASDAQ Composite Change')
plt.legend()
plt.show()



