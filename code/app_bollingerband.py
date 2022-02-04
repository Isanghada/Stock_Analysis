#ch06_06_BollingerBand_TrendFollowing
from Data import Analyzer
import pandas as pd
import datetime

import plotly
import plotly.subplots as sp
import plotly.express as px
import plotly.graph_objs as go


def trendfollowing(code):
    # 최근 6개월의 차트
    now = datetime.datetime.now()
    end = f'{now.year}-{now.month}-{now.day}'
    if(now.month < 6):
        year = now.year - 1
        month = now.month - 6 + 12
        start = f'{year}-{month}-{now.day}'
    else:
        month = now.month - 6 + 1
        start = f'{now.year}-{month}-{now.day}'

    mk = Analyzer.MarketDB()
    df = mk.get_daily_price(code, start, end)
    
    df['MA20'] = df['close'].rolling(window=20).mean() 
    df['stddev'] = df['close'].rolling(window=20).std() 
    df['upper'] = df['MA20'] + (df['stddev'] * 2)
    df['lower'] = df['MA20'] - (df['stddev'] * 2)
    df['PB'] = (df['close'] - df['lower']) / (df['upper'] - df['lower'])
    df['TP'] = (df['high'] + df['low'] + df['close']) / 3
    df['PMF'] = 0
    df['NMF'] = 0
    for i in range(len(df.close)-1):
        if df.TP.values[i] < df.TP.values[i+1]:
            df.PMF.values[i+1] = df.TP.values[i+1] * df.volume.values[i+1]
            df.NMF.values[i+1] = 0
        else:
            df.NMF.values[i+1] = df.TP.values[i+1] * df.volume.values[i+1]
            df.PMF.values[i+1] = 0
    df['MFR'] = df.PMF.rolling(window=10).sum() / df.NMF.rolling(window=10).sum()
    df['MFI10'] = 100 - 100 / (1 + df['MFR'])
    df = df[19:]

    close_fig = go.Scatter(x=df.date, y=df["close"], mode='lines', name="close", line=dict(color='blue'))
    upper_fig = go.Scatter(x=df.date, y=df["upper"], mode='lines', name="Upper band", line=dict(color='red', dash='dash'), fill ='tonexty', fillcolor='rgba(10,10,10,0.3)')
    ma20_fig = go.Scatter(x=df.date, y=df["MA20"], mode='lines', name="Moving average 20", line=dict(color='black', dash='dash'), fill ='tonexty', fillcolor='rgba(10,10,10,0.3)')
    lower_fig = go.Scatter(x=df.date, y=df["lower"], mode='lines', name="Lower band", line=dict(color='cyan', dash='dash'))

    pb_fig = go.Scatter(x=df.date, y=df["PB"] * 100, mode='lines', name="%B X 100", line=dict(color='blue'))
    mfi_fig = go.Scatter(x=df.date, y=df["MFI10"], mode='lines', name="MFI(10 day)", line=dict(color='green', dash='dash'))

    plotly_fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)
    plotly_fig.add_trace(lower_fig, row=1, col=1)
    plotly_fig.add_trace(ma20_fig, row=1, col=1)
    plotly_fig.add_trace(upper_fig, row=1, col=1)
    plotly_fig.add_trace(close_fig, row=1, col=1)
    #매수, 매도 표시
    for i in range(len(df.close)):
        if df.PB.values[i] > 0.8 and df.MFI10.values[i] > 80:
            data = df.loc[df['date']==df['date'].values[i]]
            bs_fig = go.Scatter(x=data.date, y=data.close, mode='markers', name="buy", marker=dict(color='red', symbol='arrow-up', size = 10), showlegend = False)
            plotly_fig.add_trace(bs_fig, row=1, col=1)
        elif df.PB.values[i] < 0.2 and df.MFI10.values[i] < 20:    
            data = df.loc[df['date']==df['date'].values[i]]
            bs_fig = go.Scatter(x=data.date, y=data.close, mode='markers', name="sell", marker=dict(color='blue', symbol='arrow-down', size = 10), showlegend = False)
            plotly_fig.add_trace(bs_fig, row=1, col=1)

    plotly_fig.add_trace(mfi_fig, row=2, col=1)
    plotly_fig.add_trace(pb_fig, row=2, col=1)
    #매수, 매도 표시
    zero = pd.DataFrame(data=[0], index=range(0,1), columns=['value'])
    for i in range(len(df.close)):
        if df.PB.values[i] > 0.8 and df.MFI10.values[i] > 80:
            data = df.loc[df['date']==df['date'].values[i]]
            bs_fig = go.Scatter(x=data.date, y=zero.value, mode='markers', name="buy", marker=dict(color='red', symbol='arrow-up', size = 10), showlegend = False)
            plotly_fig.add_trace(bs_fig, row=2, col=1)
        elif df.PB.values[i] < 0.2 and df.MFI10.values[i] < 20:
            data = df.loc[df['date']==df['date'].values[i]]
            bs_fig = go.Scatter(x=data.date, y=zero.value, mode='markers', name="sell", marker=dict(color='blue', symbol='arrow-down', size = 10), showlegend = False)
            plotly_fig.add_trace(bs_fig, row=2, col=1)

    plotly_fig.update_layout(
        title=f'{df.company.values[0]} Bollinger Band (20 day, 2 std) - Trend Following',
        yaxis1_title='Stock Price',
        xaxis2_title='periods',
        xaxis1_rangeslider_visible=False,
        xaxis2_rangeslider_visible=False,
        # 없는 날짜를 자동으로 생성하기 때문에 이를 없애기 위해 추가
        xaxis1 = dict(type="category", categoryorder='category ascending'),
        xaxis2 = dict(type="category", categoryorder='category ascending'),
        yaxis2 = dict(range=[-20,120])
    )
    plotly_fig.update_xaxes(nticks=5)
    return plotly_fig
    #plotly_fig.show()