import pandas as pd
import pymysql
from datetime import datetime
from datetime import timedelta
import re

class MarketDB:
    def __init__(self):
        """생성자: MariaDB 연결 및 종목코드 딕셔너리 생성"""
        self.conn = pymysql.connect(host='127.0.0.1', user='hcs', 
            password='1234', db='stock', charset='utf8')
        self.codes = {}
        self.get_comp_info()
        
    def __del__(self):
        """소멸자: MariaDB 연결 해제"""
        self.conn.close()

    def get_comp_info(self):
        """company_info 테이블에서 읽어와서 codes에 저장"""
        sql = "SELECT * FROM company_info"
        krx = pd.read_sql(sql, self.conn)
        for idx in range(len(krx)):
            self.codes[krx['code'].values[idx]] = krx['company'].values[idx]

    def get_daily_price(self, code, start_date=None, end_date=None):
        """KRX 종목의 일별 시세를 데이터프레임 형태로 반환
            - code       : KRX 종목코드('005930') 또는 상장기업명('삼성전자')
            - start_date : 조회 시작일('2020-01-01'), 미입력 시 1년 전 오늘
            - end_date   : 조회 종료일('2020-12-31'), 미입력 시 오늘 날짜
        """
        if start_date is None:
            one_year_ago = datetime.today() - timedelta(days=365)
            start_date = one_year_ago.strftime('%Y-%m-%d')
            print("start_date is initialized to '{}'".format(start_date))
        else:
            start_lst = re.split('\D+', start_date)
            if start_lst[0] == '':
                start_lst = start_lst[1:]
            start_year = int(start_lst[0])
            start_month = int(start_lst[1])
            start_day = int(start_lst[2])
            if start_year < 1900 or start_year > 2200:
                print(f"ValueError: start_year({start_year:d}) is wrong.")
                return
            if start_month < 1 or start_month > 12:
                print(f"ValueError: start_month({start_month:d}) is wrong.")
                return
            if start_day < 1 or start_day > 31:
                print(f"ValueError: start_day({start_day:d}) is wrong.")
                return
            start_date=f"{start_year:04d}-{start_month:02d}-{start_day:02d}"

        if end_date is None:
            end_date = datetime.today().strftime('%Y-%m-%d')
            print("end_date is initialized to '{}'".format(end_date))
        else:
            end_lst = re.split('\D+', end_date)
            if end_lst[0] == '':
                end_lst = end_lst[1:] 
            end_year = int(end_lst[0])
            end_month = int(end_lst[1])
            end_day = int(end_lst[2])
            if end_year < 1800 or end_year > 2200:
                print(f"ValueError: end_year({end_year:d}) is wrong.")
                return
            if end_month < 1 or end_month > 12:
                print(f"ValueError: end_month({end_month:d}) is wrong.")
                return
            if end_day < 1 or end_day > 31:
                print(f"ValueError: end_day({end_day:d}) is wrong.")
                return
            end_date = f"{end_year:04d}-{end_month:02d}-{end_day:02d}"
         
        codes_keys = list(self.codes.keys())
        codes_values = list(self.codes.values())

        if code in codes_keys:
            pass
        elif code in codes_values:
            idx = codes_values.index(code)
            code = codes_keys[idx]
        else:
            print(f"ValueError: Code({code}) doesn't exist.")
        sql = f"SELECT company_info.company, daily_price.* FROM daily_price, company_info WHERE daily_price.code = '{code}'"\
            f" and date >= '{start_date}' and date <= '{end_date}' and daily_price.code = company_info.code"
        df = pd.read_sql(sql, self.conn)
        #날짜가 중복되어 생성되므로 생략
        #df.index = df['date']
        return df 

    def get_daily_table(self):
        now = datetime.now()
        #휴일 제외 가장 최근의 날짜 확인
        if now.weekday() == 0:
            if now.day <= 3:
                if(now.month == 2):
                    now = f'{now.year}-{now.month-1}-{now.day-3+28}'
                else:
                    now = f'{now.year}-{now.month-1}-{now.day-3+30}'
            else :
                now = f'{now.year}-{now.month}-{now.day-3}'
        elif now.weekday() == 6:
            if now.day <= 2:
                if(now.month == 2):
                    now = f'{now.year}-{now.month-1}-{now.day-2+28}'
                else:
                    now = f'{now.year}-{now.month-1}-{now.day-2+30}'
            else :
                now = f'{now.year}-{now.month}-{now.day-2}'
        else:
            if now.day <= 1:
                if(now.month == 2):
                    now = f'{now.year}-{now.month-1}-{now.day-1+28}'
                else:
                    now = f'{now.year}-{now.month-1}-{now.day-1+30}'
            else :
                now = f'{now.year}-{now.month}-{now.day-1}'
        #가장 최근의 종가 추출
        sql = f"SELECT company_info.company, daily_price.close, daily_price.volume FROM daily_price, company_info WHERE daily_price.date = '{now}' and daily_price.code = company_info.code"
        table = pd.read_sql(sql, self.conn)
        return table