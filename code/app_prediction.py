#ch09_09_RNN_StockPrediction
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
import numpy as np
import pandas as pd
from Data import Analyzer

import plotly
import plotly.subplots as sp
import plotly.express as px
import plotly.graph_objs as go

mk = Analyzer.MarketDB()

def MinMaxScaler(data):
    """최솟값과 최댓값을 이용하여 0 ~ 1 값으로 변환"""
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    # 0으로 나누기 에러가 발생하지 않도록 매우 작은 값(1e-7)을 더해서 나눔
    return numerator / (denominator + 1e-7)

def predict_stock(code):
    raw_df = mk.get_daily_price(code, '2018-06-01')

    window_size = 10 
    data_size = 5
    company = raw_df.company.values[0]
    dfx = raw_df[['open','high','low','volume', 'close']]
    dfx = MinMaxScaler(dfx)
    dfy = dfx[['close']]

    x = dfx.values.tolist()
    y = dfy.values.tolist()

    data_x = []
    data_y = []
    for i in range(len(y) - window_size):
        _x = x[i : i + window_size] # 다음 날 종가(i+windows_size)는 포함되지 않음
        _y = y[i + window_size]     # 다음 날 종가
        data_x.append(_x)
        data_y.append(_y)
    print(_x, "->", _y)

    train_size = int(len(data_y) * 0.7)
    train_x = np.array(data_x[0 : train_size])
    train_y = np.array(data_y[0 : train_size])

    test_size = len(data_y) - train_size
    test_x = np.array(data_x[train_size : len(data_x)])
    test_y = np.array(data_y[train_size : len(data_y)])

    # 모델 생성
    model = Sequential()
    model.add(LSTM(units=10, activation='relu', return_sequences=True, input_shape=(window_size, data_size)))
    model.add(Dropout(0.1))
    model.add(LSTM(units=10, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(units=1))
    model.summary()

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(train_x, train_y, epochs=70, batch_size=30)
    pred_y = model.predict(test_x)
    pre_df = pd.DataFrame(test_y)
    pre_df = pre_df.rename(columns = {0 : 'real'})
    pre_df['predict'] = pred_y
    #print(pre_df)
    predict = round(float((raw_df.close[len(raw_df)-1] * pred_y[-1]) / dfy.close[len(dfy)-1]), 0)
    print(f"Tomorrow's {company} price : {predict} KRW")

    '''real_fig = go.Scatter(x= pre_df.index, y=pre_df.real, name="Real", line=dict(color='blue'))
    pred_fig = go.Scatter(x= pre_df.index, y=pre_df.predict, name="Predict", line=dict(color='red'))
    layout = go.Layout(title='Stock Price Prediction Test', xaxis_title = 'Times', yaxis_title = 'Value', xaxis_rangeslider_visible=True)

    plotly_fig = go.Figure(data = [real_fig, pred_fig], layout = layout)
    plotly_fig.update_xaxes(nticks=10)

    plotly_fig.show()'''

    pre_return = [company, predict]

    return pre_return