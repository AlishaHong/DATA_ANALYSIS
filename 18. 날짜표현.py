# -*- coding: utf-8 -*-
# 날짜 표현
# 월별, 일별, 요일별 집계
# 현재날짜 - 입사일자 : 근무일수 

# 1. 현재 날짜 
run my_profile
from datetime import datetime

d1 = datetime.now()   # 현재 날짜(시간 포함)
type(d1)              # 데이터 타입 확인

d1.year               # 년
d1.month              # 월
d1.day                # 일
d1.hour               # 시간

# 2. 날짜 파싱(날짜로 인지되지 않은 데이터를 날짜로 인지시키는 행위)
d2 = '2021/01/01'
d2.year               # d2가 아직 날짜 데이터가 아니기 때문에 출력 불가

# 1) datetime.strptime
# 벡터 연산 불가
datetime.strptime(d2, '%Y/%m/%d')    # 두번째 인수(생략 불가)는 앞의 문자열을 어떤 날짜 타입으로 해석해야하는지를 알려주는 지표

datetime.strptime('09/12/08', '%y/%m/%d')    # 09년 12월 8일로 해석
datetime.strptime('09/12/08', '%m/%d/%y')    # 08년 9월 12일로 해석

s1 = Series(['2021/01/01', '2021/01/02', '2021/01/03'])
datetime.strptime(s1, '%Y/%m/%d')                          # 벡터 연산 불가
s1.map(lambda x : datetime.strptime(x, '%Y/%m/%d'))        # map을 사용한 벡터 연산 처리

# 2) pd.to_datetime
# 벡터 연산 가능
pd.to_datetime(s1)                             # 날짜포맷을 생략해도 파싱 가능(자동으로 년/월/일로 해석)
s2 = pd.to_datetime(s1, format='%Y/%m/%d')     # 날짜포맷을 전달할 경우 format=''으로 전달 필요

# 3. 날짜 포맷 변경
# 요일추출(날짜에서 요일을 리턴하도록 날짜 출력 형식을 변경)
# (년/월/일 => 월/일/년 순서로 변경)
# 날짜 포맷 변경 후 리턴 데이터 타입은 무조건 문자!

datetime.strftime(d1, '%A')               # 요일 리턴
datetime.strftime(d1, '%m-%d,%Y')         # 리턴하고자 할 날짜 포맷 전달

datetime.strftime(d1, '%Y')               # 문자열로 리턴

datetime.strftime(s2, '%Y')                    # 벡터 연산 불가
s2.map(lambda x : datetime.strftime(x, '%Y'))  # 벡터 연산 가능


# 4. 날짜 연산
d1 + 100                         # 오늘날짜로부터 100일 뒤 날짜 리턴(불가)

# 1) offset
from pandas.tseries.offsets import Day, Hour, Second
d1 + Day(100)                    # 오늘날짜로부터 100일 뒤 날짜 리턴

# 2) timedelta
from datetime import timedelta
d1 + timedelta(100)              # 오늘날짜로부터 100일 뒤 날짜 리턴

# 3) DateOffset**
d1 + pd.DateOffset(months=3)     # 3개월 뒤 날짜 리턴

# 5. 날짜 - 날짜
d1 - datetime.strptime(d2, '%Y/%m/%d')         # 두 날짜 사이의 일 수, 초 리턴
d3 = d1 - datetime.strptime(d2, '%Y/%m/%d')    # 두 날짜 사이의 일 수, 초 리턴
d3.days                                        # 두 날짜 사이의 일 수 리턴

# [ 참고 - 날짜 포맷 확인 ]
import time
time.strptime? 


# [ 연습 문제 - delivery.csv 파일을 읽고 요일별 통화건수 총 합 ]
deli = pd.read_csv('delivery.csv', encoding='cp949')

deli.dtypes

# 날짜 파싱
deli['일자'] = pd.to_datetime(deli['일자'], format='%Y%m%d')

# 요일 리턴
datetime.strftime(deli['일자'], '%A')                                    # 불가
deli['요일'] = deli['일자'].map(lambda x : datetime.strftime(x, '%A'))   # 가능

# 요일별 그룹핑
total = deli.groupby('요일')['통화건수'].sum()

total[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]   # 월화수목금토일 순으로 재배치(정렬로 불가, 색인으로 처리 가능)

