#ch04_03_Celltrion_CandleChart_NewSchool
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from Data import Analyzer

import plotly
import plotly.subplots as sp
import plotly.express as px
import plotly.graph_objs as go

import datetime

def candlechart(code):
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
    company = df.company.values[0]
    df = df.dropna()

    df = df.sort_values(by='date')
    df = df[['date', 'open', 'high', 'low', 'close', 'volume']]

    candle = go.Candlestick(x=df.date,
                        open=df.open,
                        high=df.high,
                        low=df.low,
                        close=df.close,
                        name = 'Stock Price',
                        increasing_line_color = 'red',
                        decreasing_line_color = 'blue')

    volume = go.Bar(x=df.date, y=df['volume'], name = 'Volume')
    
    # 일간 주가 캔들차트 + 거래량
    plotly_fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.02)
    plotly_fig.add_trace(candle, row=1, col=1)
    plotly_fig.add_trace(volume, row=2, col=1)
    plotly_fig.update_layout(
        title=f'{company} Candle Chart',
        yaxis1_title='Stock Price',
        yaxis2_title='Volume',
        xaxis2_title='Periods',
        xaxis1_rangeslider_visible=False,
        xaxis2_rangeslider_visible=True,
        # 없는 날짜를 자동으로 생성하기 때문에 이를 없애기 위해 추가
        xaxis1 = dict(type="category", categoryorder='category ascending'),
        xaxis2 = dict(type="category", categoryorder='category ascending')
    )
    plotly_fig.update_xaxes(nticks=5)
    return plotly_fig