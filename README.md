# ๐์ฃผ์ ๋ถ์ ๋ฐ ์์ธก ํ๋ก์ ํธ
## Introduction
- **์ฃผ์ ๋ฐ์ดํฐ ๋ถ์ ๋ฐ ์์ธก**์ ํตํ ์ ๋ณด ์ ๊ณต์ ๋ชฉ์ ์ผ๋ก ์งํํ ํ๋ก์ ํธ์๋๋ค.
- ์์๊ฐ, ์ ๊ฐ, ๊ณ ๊ฐ, ์ข๊ฐ, ๊ฑฐ๋๋ ๋ฑ์ ์ปฌ๋ผ์ ํตํด **์ฃผ๊ฐ ๋ฐ์ดํฐ ๋ถ์** ๋ฐ **์๊ณ์ด ์์ธก์ ํตํด ์ข๊ฐ ์์ธก**์ ์งํํ๋ค.
- ๊ตฌํ ๊ฒฐ๊ณผ  
  ![image](https://user-images.githubusercontent.com/90487843/153156062-894cfee3-65c3-48f3-b9ab-70071770cf83.png)

## Contents
- [1. ํ๋ก์ ํธ ์๊ฐ](#1-ํ๋ก์ ํธ-์๊ฐ) 
- [2. ๋ฐ์ดํฐ ์์ง ๋ฐ ์ ์ฅ](#2-๋ฐ์ดํฐ-์์ง-๋ฐ-์ ์ฅ)
- [3. ์์คํ ๊ตฌํ](#3-์์คํ-๊ตฌํ)
  - [์บ๋ค ์ฐจํธ](#์บ๋ค-์ฐจํธ)
  - [์ถ์ธ ์ถ์ข ๊ธฐ๋ฒ](#์ถ์ธ-์ถ์ข-๊ธฐ๋ฒ)
  - [์ข๊ฐ ์๊ณ์ด ์์ธก](#์ข๊ฐ-์๊ณ์ด-์์ธก)
- [4. ์ต์ข ์์คํ](#4-์ต์ข-์์คํ)
- [5. ํ๊ณ ๋ฐ ๋ณด์์ ](#5-ํ๊ณ-๋ฐ-๋ณด์์ )
- [6. ์ฐธ๊ณ  ์๋ฃ](#6-์ฐธ๊ณ -์๋ฃ)
- [7. ๊ตฌ์ฑ ์ธ์](#7-๊ตฌ์ฑ-์ธ์)

## 1. ํ๋ก์ ํธ ์๊ฐ
### ๋ฐฐ๊ฒฝ
- ๊ณผ๊ฑฐ ์ํ ์ ์ถ, ๋จ์ํ ์ ์ถ ์ฉ๋๋ก ๋ง์ด ์ฌ์ฉ | ์ฃผ์  ๋งค์, ๋งค๋๋ฅผ ํตํ ์์ธ ์ฐจ์ต ์ฑํ
- ์ ๋ณด์ ๋ถ์กฑ์ผ๋ก ์ง์์ ์ด๋ ค์์ด ์กด์ฌ
- ์ฃผ์ ๋ถ์ ์ ๋ณด ์ ๊ณต์ ํตํด ํจ์จ์ ์ธ ํฌ์๊ฐ ๊ฐ๋ฅํด์ง ๊ฒ

### ํ๋ก์ ํธ ๊ฐ์
- ๊ตฌ์ฑ์ธ์ : ๊น๋จ๊ท, ์ต์์ฐ, ํ
- ์ํ๊ธฐ๊ฐ : 3๋ฌ (2021๋ 3์ ~ 2021๋ 6์)
- ๋ชฉํ : ์ฃผ์ ์ ๋ณด ๋ถ์ ๋ฐ ์ข๊ฐ ์์ธก
- ๋ฐ์ดํฐ : KRX ์์ฅ ๊ธฐ์ ์ฝ๋, ๋ค์ด๋ฒ ์ฃผ์ ๋ฐ์ดํฐ

### ๊ฐ๋ฐ ํ๊ฒฝ
- ์ธ์ด : Python, MariaDB(SQL)
- ๋ผ์ด๋ธ๋ฌ๋ฆฌ : **Pandas**, **Numpy**, **Pandas**, **Plotly**, **BeautifulSoup4**, **Tensorflow**
- ์๊ณ ๋ฆฌ์ฆ : LSTM(์๊ณ์ด ์์ธก)

## 2. ๋ฐ์ดํฐ ์์ง ๋ฐ ์ ์ฅ
#### โชKRX ์์ฅ ๊ธฐ์ ์ฝ๋
- https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage     
- ์์ฅ ๊ธฐ์ ์ฝ๋ ์ ์ฒด๋ฅผ EXCEL ํ์ผ๋ก ํ๋  
<img src="https://user-images.githubusercontent.com/90487843/153339736-92b65aa5-cddf-421a-bc2b-71335c6ac90e.png" width="70%" height="70%">  

#### โช๋ค์ด๋ฒ ์ฃผ์ ๋ฐ์ดํฐ    
- `https://finance.naver.com/item/sise_day.nhn?code=๊ธฐ์ ์ฝ๋`  
- ex) https://finance.naver.com/item/sise_day.nhn?code=000020     
- BeautifulSoup๋ฅผ ์ด์ฉํด ๊ฐ ๊ธฐ์์ ์ฃผ์ ์ ๋ณด ํ๋  
<img src="https://user-images.githubusercontent.com/90487843/153339087-ad9df838-4857-4af6-af1a-c598eecec720.png" width="70%" height="70%">

#### โช๋ฐ์ดํฐ ์ ์ฅ
- ์์ฅ ๊ธฐ์ ์ฝ๋์ ์ฃผ์ ๋ฐ์ดํฐ๋ DB์ ์ ์ฅ
- ์์ฅ ๊ธฐ์ ์ฝ๋
  - code : ๊ธฐ์ ์ฝ๋
  - company : ๊ธฐ์๋ช
  - last_update : ์ต๊ทผ ์๋ฐ์ดํธ ๋ ์ง  
![company](https://user-images.githubusercontent.com/90487843/153340785-93862290-9bbf-41db-8654-357da75d32cd.png)
- ์ฃผ๊ฐ ์ผ์ผ ์ ๋ณด   
  - code : ๊ธฐ์ ์ฝ๋
  - date : ๋ ์ง
  - open : ์์๊ฐ
  - high : ๊ณ ๊ฐ
  - low : ์ ๊ฐ
  - close : ์ข๊ฐ
  - diff : ์ข๊ฐ ์ฐจ์ด
  - volume : ๊ฑฐ๋๋  
    <img src="https://user-images.githubusercontent.com/90487843/153340914-0368579e-639e-4877-9147-55812a093b67.png" width="50%" height="50%">  

## 3. ์์คํ ๊ตฌํ
### ์บ๋ค ์ฐจํธ
- Plotly๋ฅผ ํตํด ์บ๋ค ์ฐจํธ ๊ตฌํ
  - ์์๊ฐ, ๊ณ ๊ฐ, ์ ๊ฐ, ์ข๊ฐ ์ปฌ๋ผ ํ์ฉ  
  <img src="https://user-images.githubusercontent.com/90487843/153736818-c0cd0031-e625-4819-8071-74dd65f517dc.png" width="70%" height="70%">

```python
import plotly
import plotly.subplots as sp
import plotly.express as px
import plotly.graph_objs as go

candle = go.Candlestick(x=df.date,
                        open=df.open,
                        high=df.high,
                        low=df.low,
                        close=df.close,
                        name = 'Stock Price',
                        increasing_line_color = 'red',
                        decreasing_line_color = 'blue')

volume = go.Bar(x=df.date, y=df['volume'], name = 'Volume')

# ์ผ๊ฐ ์ฃผ๊ฐ ์บ๋ค์ฐจํธ + ๊ฑฐ๋๋
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
    # ์๋ ๋ ์ง๋ฅผ ์๋์ผ๋ก ์์ฑํ๊ธฐ ๋๋ฌธ์ ์ด๋ฅผ ์์ ๊ธฐ ์ํด ์ถ๊ฐ
    xaxis1 = dict(type="category", categoryorder='category ascending'),
    xaxis2 = dict(type="category", categoryorder='category ascending')
)
```  

### ์ถ์ธ ์ถ์ข ๊ธฐ๋ฒ
- ์ปฌ๋ผ๋ค์ ์ด์ฉํด ๋ณด์กฐ ์งํ ๊ณ์ฐ
  - DataFrame์ rolling์ ์ด์ฉํด ์ด๋ํ๊ท  ๊ณ์ฐ

```python
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
```

- ๋ณผ๋ฆฐ์  ๋ฐด๋ ์ฐจํธ๋ฅผ ์ด์ฉํด ์ถ์ธ ์ถ์ข ๊ธฐ๋ฒ ์๊ฐํ  
<img src = "https://user-images.githubusercontent.com/90487843/153736881-82bcb06e-8daa-4abf-8bf6-f680a4655282.png" width="70%" height="70%">

```python
import plotly
import plotly.subplots as sp
import plotly.express as px
import plotly.graph_objs as go

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
```

### ์ข๊ฐ ์๊ณ์ด ์์ธก 
- ์ข๊ฐ ์๊ณ์ด ์์ธก : **Tensorflow๋ฅผ ์ด์ฉํด ๊ตฌํ**
  - open, high, low, close, diff, volume ์ปฌ๋ผ ์ด์ฉ
  - LSTM Layer ์ฌ์ฉ -> ์๊ณ์ด ์์ธก  
  <img src="https://user-images.githubusercontent.com/90487843/153738546-86820808-e6be-42f6-8e51-ae6ea6396fc9.png" width="35%" height="35%">  

```python
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

# ๋ชจ๋ธ ์์ฑ
model = Sequential()
model.add(LSTM(units=10, activation='relu', return_sequences=True, input_shape=(window_size, data_size)))
model.add(Dropout(0.1))
model.add(LSTM(units=10, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(units=1))
model.compile(optimizer='adam', loss='mean_squared_error')

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(train_x, train_y, epochs=70, batch_size=30)
pred_y = model.predict(test_x)
pre_df = pd.DataFrame(test_y)
pre_df = pre_df.rename(columns = {0 : 'real'})
pre_df['predict'] = pred_y

predict = round(float((raw_df.close[len(raw_df)-1] * pred_y[-1]) / dfy.close[len(dfy)-1]), 0)
```

## 4. ์ต์ข ์์คํ
- ๋ฐ์ดํฐ ํ๋
  - KRX ์์ฅ ๊ธฐ์ ๋ฐ์ดํฐ
  - ๋ค์ด๋ฒ ์ฃผ์ ๋ฐ์ดํฐ -> DB ์ ์ฅ
- ๋ฐ์ดํฐ ๋ถ์ ๋ฐ ์๊ฐํ
  - ์บ๋ค ์ฐจํธ
  - ์ถ์ธ ์ถ์ข ๊ธฐ๋ฒ -> ๋ณผ๋ฆฐ์  ๋ฐด๋ ์ฐจํธ
- ์ข๊ฐ ์์ธก
  - LSTM Layer ์ฌ์ฉ ์๊ณ์ด ์์ธก
- ์น ํ์ด์ง ๊ตฌํ
  - Dash๋ฅผ ์ด์ฉํด ๊ตฌํ
  - ๋๋กญ ์์ ๋ผ๋ฒจ์ ํตํด ์์ฅ ๊ธฐ์(์ฝ๋) ์ ํ
  - ๋ถ์ ๋ฐ ์์ธก ์ ๋ณด ์ถ๋ ฅ
### ์์คํ ๋์ ์์
1. ๊ธฐ์(์ฝ๋) ์ ํ : ๋๋กญ ์์ ๋ผ๋ฒจ
2. ๋ถ์ ๋ฐ ์์ธก ๊ฒฐ๊ณผ ์ถ๋ ฅ : ์บ๋ค ์ฐจํธ, ๋ณผ๋ฆฐ์  ๋ฐด๋ ์ฐจํธ, ์ข๊ฐ ์์ธก

<img src="https://user-images.githubusercontent.com/90487843/153810887-3a75569d-5d83-4974-82ca-9634f3b94618.png" width="85%" height = "85%">


## 5. ํ๊ณ ๋ฐ ๋ณด์์ 
#### ๐ ๋ฐ์ดํฐ
- ์ผ๊ฐ ์ ๋ณด๋ง์ ์ด์ฉํด ๋ถ์๊ณผ ์์ธก์ ์งํํ์๋ค.
  - ์ผ๊ฐ ์ ๋ณด๋ง์ผ๋ก ์ ์ฒด ๊ฒฝํฅ์ ํ๋จํ๊ธฐ์๋ ๋ถ์กฑํ๋ค.
  - ์๊ฐ, ๋๊ฐ ๋ฑ์ ์ ๋ณด ์ถ๊ฐ ํ์ฉ์ด ํ์ํ๋ค.
- ์ฃผ๊ฐ ์ ๋ณด๋ก๋ ๊ธฐ์ ์ด๋ฏธ์ง ํ๋จ์ด ๋ถ๊ฐ๋ฅํ๋ค.
  - ๊ธฐ์์ ๋ํ ๋ด์ค ๊ธฐ์ฌ ๊ฐ์ฑ ๋ถ์์ ํตํด ๋ณด์ํ  ์ ์๋ค.
#### ๐ ๋ถ์ ๋ฐฉ์ ๋ค์ํ
- ์ถ์ธ ์ถ์ข ๊ธฐ๋ฒ, ์๊ณ์ด ์์ธก 2๊ฐ์ง ๋ฐฉ๋ฒ๋ง์ ์ฌ์ฉํ์๋ค.
- ์ฃผ์์ ๋ถ์ํ๋ ๋ฐฉ๋ฒ์ ์ถ๊ฐ๋ก ๊ตฌํํ์ฌ ๋ค์ํ ๋ถ์ ๊ฒฐ๊ณผ๋ฅผ ๋ณด์ฌ์ค ์ ์๋ค.

## 6. ์ฐธ๊ณ  ์๋ฃ
- ๊นํฉํ, โํ์ด์ฌ ์ฆ๊ถ ๋ฐ์ดํฐ ๋ถ์โ, โํ๋น๋ฏธ๋์ดโ, 2020
- ์กด ๋ณผ๋ฆฐ์ , โ๋ณผ๋ฆฐ์  ๋ฐด๋ ํฌ์๊ธฐ๋ฒโ, โ์ด๋ ๋ฏธ๋์ดโ, 2010
- ๊นํํฌ, โํ์ํ๋ก 2.0 ํ๋ก๊ทธ๋๋ฐโ, โ์ํค๋ถ์คโ, 2020
- Dash ๊ณต์ ๋ฌธ์ : https://dash.plotly.com/
- Plotly ๊ณต์ ๋ฌธ์ : https://plotly.com/python-api-reference/
- Tensorflow ๊ณต์ ๋ฌธ์ : https://www.tensorflow.org/api_docs/python/tf?hl=ko

## 7. ๊ตฌ์ฑ ์ธ์
- ๊น๋จ๊ท : <a href = 'https://github.com/Isanghada' target='_blink'>Github</a>
- ์ต์์ฐ
- ํ์ฐฝ์ฌ
