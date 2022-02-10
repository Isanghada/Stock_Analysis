# 📈주식 분석 및 예측 프로젝트
## Introduction
- **주식 데이터 분석 및 예측**을 통한 정보 제공을 목적으로 진행한 프로젝트입니다.
- 시작가, 저가, 고가, 종가, 거래량 등의 컬럼을 통해 **주가 데이터 분석** 및 **시계열 예측을 통해 종가 예측**을 진행한다.
- 구현 결과  
  ![image](https://user-images.githubusercontent.com/90487843/153156062-894cfee3-65c3-48f3-b9ab-70071770cf83.png)

## Contents
- [1. 프로젝트 소개](#1-프로젝트-소개) 
- [2. 데이터 수집 및 저장](#2-데이터-수집-및-저장)
- [3. 모델링](#3-모델링)
  - [이미지 특징 추출 및 유사도 측정](#이미지-특징-추출-및-유사도-측정)
  - [음식 라벨링](#음식-라벨링)
  - [테마 자연어 유사도](#테마-자연어-유사도)
  - [경로 추천](#경로-추천)
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
- 구성인원 : 김남규, 최◯◯, 한◯◯
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

## 3. 모델링
### 이미지 특징 추출 및 유사도 측정
- ㅇㅅㅇ

### 음식 라벨링
- ㅇㅅㅇ

### 테마 자연어 유사도
- ㅇㅅㅇ

### 경로 추천
- ㅇㅅㅇ

## 4. 최종 시스템
ㅇㅅㅇ  
### 시스템 동작 예시
#### 1) 키워드 선택
#### 2) 카테고리 선택
#### 3) 대표 장소 선택(카페일 경우 실행X)
#### 4) 관광지 추천
#### 5) 경로 탐색
#### 6) 경로 출력

## 5. 한계 및 보완점
#### 🛠사용 데이터 부족
- ㅇㅅㅇ

## 6. 참고 자료
- ㅇㅅㅇ

## 7. 구성 인원
- 김남규 : <a href = 'https://github.com/Isanghada' target='_blink'>Github</a>
- 최◯◯
- 한◯◯
