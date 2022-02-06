# 소스 코드
### 1. Data/Analyzer.py
- DB에 접근하기 위해 `MarketDB` 클래스 정의
  - DB에 저장된 주식 정보를 DataFrame으로 반환하는 함수로 구성
  - `기업 코드`, `기업명`, `저가`, `고가`, `종가`, `거래량` 등의 컬럼 반환
- 전체 기업에 대한 주가 정보 반환 함수 : `get_daily_table()`
- 특정 기업에 대한 주가 정보 반환 함수 : `get_daily_price(기업 코드, 조회 시작일, 조회 종료일)`
---
### 2. Data/DBUpdater.py
- 주식 데이터 수집을 위해 `DBUpdater` 클래스 정의
  - 상장 기업 코드와 `BeautifulSoup`를 이용해 네이버 주식 데이터 추출
  - 추출 데이터 DB에 저장
- 상장 기업 코드 : KRX 데이터
  - https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage'
- 주식 정보 : 네이버 주식 데이터
  - `https://finance.naver.com/item/sise_day.nhn?code=기업 코드`
  - ex) https://finance.naver.com/item/sise_day.nhn?code=00000
- 데이터 저장 : MariaDB를 활용하여 추출한 데이터 저장
---
### 3. app_bollingerband.py
- 볼린저 밴드
---
### 4. app_candlechart.py
- 캔들 차트
---
### 5. app_prediction.py
- 종가 예측
---
### 6. app_v1.2.py
- 웹 표현
- 로컬 확인
---
