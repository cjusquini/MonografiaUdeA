# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU, Dense, Flatten, Dropout
# from tensorflow.keras.models import Model
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error

def create_sequences(data, n_lag, target_column):
    sequences = []
    targets = []
    for i in range(len(data) - n_lag):
        seq = data[i:i + n_lag]
        target = data[i + n_lag][target_column]
        sequences.append(seq)
        targets.append(target)
    return np.array(sequences), np.array(targets)

def split_data(lags, scaled_df, train_test_split_ratio = 0.7):
  lagged_data = {}
  for lag in lags:
      X, y = create_sequences(scaled_df.values, lag, target_column=0)
      lagged_data[lag] = (X, y)

  train_test_split_ratio = train_test_split_ratio
  split_idx = int(len(scaled_df) * train_test_split_ratio)

  train_data = {lag: (X[:split_idx], y[:split_idx]) for lag, (X, y) in lagged_data.items()}
  test_data = {lag: (X[split_idx:], y[split_idx:]) for lag, (X, y) in lagged_data.items()}

  return train_data, test_data

def get_metrics(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    mape = mean_absolute_percentage_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    return mae, mse, mape, rmse

def create_model(model_type, input_shape, elements_to_predict, optimizer, loss, neuronas = 20):
    tf.keras.backend.clear_session()
    model = Sequential()
    if model_type == 'RNN':
        model.add(SimpleRNN(neuronas, input_shape=input_shape))
        model.add(Flatten())
        model.add(Dropout(0.3))
        model.add(Dense(20, activation='relu'))
        model.add(Dropout(0.3))

    elif model_type == 'DNN':
        model.add(Dense(neuronas, input_shape=input_shape))
        model.add(Flatten())
        model.add(Dropout(0.3))
        model.add(Dense(20, activation='relu'))
        model.add(Dropout(0.3))

    elif model_type == 'LSTM':
        model.add(LSTM(neuronas, input_shape=input_shape))
        model.add(Flatten())
        model.add(Dropout(0.3))
        model.add(Dense(20, activation='relu'))
        model.add(Dropout(0.3))

    elif model_type == 'GRU':
        model.add(GRU(neuronas, input_shape=input_shape))
        model.add(Flatten())
        model.add(Dropout(0.3))
        model.add(Dense(20, activation='relu'))
        model.add(Dropout(0.3))

    model.add(Dense(1))
    model.compile(optimizer = optimizer, loss = loss)
    print(f"Model {model_type} created. Params -> input_shape: {input_shape}, elements_to_predict: {elements_to_predict}, optimizer: {optimizer}, loss: {loss}")
    return model

