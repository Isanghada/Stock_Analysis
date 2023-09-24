# 📈주식 분석 및 예측 프로젝트
## Introduction
- **주식 데이터 분석 및 예측**을 통한 정보 제공을 목적으로 진행한 프로젝트입니다.
- 시작가, 저가, 고가, 종가, 거래량 등의 컬럼을 통해 **주가 데이터 분석** 및 **시계열 예측을 통해 종가 예측**을 진행한다.
- 구현 결과  
  ![image](https://user-images.githubusercontent.com/90487843/153156062-894cfee3-65c3-48f3-b9ab-70071770cf83.png)

## Contents
- [1. 프로젝트 소개](#1-프로젝트-소개) 
- [2. 데이터 수집 및 저장](#2-데이터-수집-및-저장)
- [3. 시스템 구현](#3-시스템-구현)
  - [캔들 차트](#캔들-차트)
  - [추세 추종 기법](#추세-추종-기법)
  - [종가 시계열 예측](#종가-시계열-예측)
- [4. 최종 시스템](#4-최종-시스템)
- [5. 한계 및 보완점](#5-한계-및-보완점)
- [6. 참고 자료](#6-참고-자료)
- [7. 구성 인원](#7-구성-인원)

## 1. 프로젝트 소개
### 배경
- 과거 은행 저축, 단순히 저축 용도로 많이 사용 | 주식  매수, 매도를 통한 시세 차익 성행
- 정보의 부족으로 진입의 어려움이 존재
- 주식 분석 정보 제공을 통해 효율적인 투자가 가능해질 것

### 프로젝트 개요
- 구성인원 : 김남규, 최원우, 한창재
- 수행기간 : 3달 (2021년 3월 ~ 2021년 6월)
- 목표 : 주식 정보 분석 및 종가 예측
- 데이터 : KRX 상장 기업 코드, 네이버 주식 데이터

### 개발 환경
- 언어 : Python, MariaDB(SQL)
- 라이브러리 : **Pandas**, **Numpy**, **Pandas**, **Plotly**, **BeautifulSoup4**, **Tensorflow**
- 알고리즘 : LSTM(시계열 예측)

## 2. 데이터 수집 및 저장
#### ▪KRX 상장 기업 코드
- https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage     
- 상장 기업 코드 전체를 EXCEL 파일로 획득  
<img src="https://user-images.githubusercontent.com/90487843/153339736-92b65aa5-cddf-421a-bc2b-71335c6ac90e.png" width="70%" height="70%">  

#### ▪네이버 주식 데이터    
- `https://finance.naver.com/item/sise_day.nhn?code=기업 코드`  
- ex) https://finance.naver.com/item/sise_day.nhn?code=000020     
- BeautifulSoup를 이용해 각 기업의 주식 정보 획득  
<img src="https://user-images.githubusercontent.com/90487843/153339087-ad9df838-4857-4af6-af1a-c598eecec720.png" width="70%" height="70%">

#### ▪데이터 저장
- 상장 기업 코드와 주식 데이터는 DB에 저장
- 상장 기업 코드
  - code : 기업 코드
  - company : 기업명
  - last_update : 최근 업데이트 날짜  
![company](https://user-images.githubusercontent.com/90487843/153340785-93862290-9bbf-41db-8654-357da75d32cd.png)
- 주가 일일 정보   
  - code : 기업 코드
  - date : 날짜
  - open : 시작가
  - high : 고가
  - low : 저가
  - close : 종가
  - diff : 종가 차이
  - volume : 거래량  
    <img src="https://user-images.githubusercontent.com/90487843/153340914-0368579e-639e-4877-9147-55812a093b67.png" width="50%" height="50%">  

## 3. 시스템 구현
### 캔들 차트
- Plotly를 통해 캔들 차트 구현
  - 시작가, 고가, 저가, 종가 컬럼 활용  
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
```  

### 추세 추종 기법
- 컬럼들을 이용해 보조 지표 계산
  - DataFrame의 rolling을 이용해 이동평균 계산

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

- 볼린저 밴드 차트를 이용해 추세 추종 기법 시각화  
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

### 종가 시계열 예측 
- 종가 시계열 예측 : **Tensorflow를 이용해 구현**
  - open, high, low, close, diff, volume 컬럼 이용
  - LSTM Layer 사용 -> 시계열 예측  
  <img src="https://user-images.githubusercontent.com/90487843/153738546-86820808-e6be-42f6-8e51-ae6ea6396fc9.png" width="35%" height="35%">  

```python
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout

# 모델 생성
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

## 4. 최종 시스템
- 데이터 획득
  - KRX 상장 기업 데이터
  - 네이버 주식 데이터 -> DB 저장
- 데이터 분석 및 시각화
  - 캔들 차트
  - 추세 추종 기법 -> 볼린저 밴드 차트
- 종가 예측
  - LSTM Layer 사용 시계열 예측
- 웹 페이지 구현
  - Dash를 이용해 구현
  - 드롭 아웃 라벨을 통해 상장 기업(코드) 선택
  - 분석 및 예측 정보 출력
### 시스템 동작 예시
1. 기업(코드) 선택 : 드롭 아웃 라벨
2. 분석 및 예측 결과 출력 : 캔들 차트, 볼린저 밴드 차트, 종가 예측

<img src="https://user-images.githubusercontent.com/90487843/153810887-3a75569d-5d83-4974-82ca-9634f3b94618.png" width="85%" height = "85%">


## 5. 한계 및 보완점
#### 🛠데이터
- 일간 정보만을 이용해 분석과 예측을 진행하였다.
  - 일간 정보만으로 전체 경향을 판단하기에는 부족하다.
  - 월간, 년간 등의 정보 추가 활용이 필요하다.
- 주가 정보로는 기업 이미지 판단이 불가능하다.
  - 기업에 대한 뉴스 기사 감성 분석을 통해 보완할 수 있다.
#### 🛠분석 방식 다양화
- 추세 추종 기법, 시계열 예측 2가지 방법만을 사용하였다.
- 주식을 분석하는 방법을 추가로 구현하여 다양한 분석 결과를 보여줄 수 있다.

## 6. 참고 자료
- 김황후, “파이썬 증권 데이터 분석”, “한빛미디어”, 2020
- 존 볼린저, “볼린저 밴드 투자기법”, “이레미디어”, 2010
- 김환희, “텐서플로 2.0 프로그래밍”, “위키북스”, 2020
- Dash 공식 문서 : https://dash.plotly.com/
- Plotly 공식 문서 : https://plotly.com/python-api-reference/
- Tensorflow 공식 문서 : https://www.tensorflow.org/api_docs/python/tf?hl=ko

## 7. 구성 인원
- 김남규 : <a href = 'https://github.com/Isanghada' target='_blink'>Github</a>
- 최원우
- 한창재
