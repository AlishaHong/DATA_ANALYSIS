# -*- coding: utf-8 -*-

# 행이 서로 분리되어 있는 경우 하나의 데이터 프레임으로 합치기
# 컬럼이 서로 분리되어 있는 경우 하나의 데이터 프레임으로 합치기
# 참조 조건을 사용하여 연관된 두 데이터를 병합하기(조인)

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(1,7).reshape(2,3), columns = ['A', 'B', 'C'])
df2 = DataFrame(np.arange(10,61,10).reshape(2,3), columns = ['A', 'B', 'C'])

pd.concat([df1, df2])                          # 기본은 세로 방향으로 합쳐짐(행의 결합)
pd.concat([df1, df2], ignore_index = True)     # ignore_index = True 을 통해서 순차적 인덱스 번호 부여 가능
pd.concat([df1, df2], axis = 1)                # 가로 방향으로 합쳐짐(컬럼의 결합)

고객에 대한 정보
file1(고객번호 1 ~ 1000)
file2(고객번호 1001 ~ 2000)

# 조인
# 두 데이터프레임(테이블)의 참조 조건을 활용하여 하나의 객체로 합치거나 데이터 처리를 하는 행위
# merge가 두 데이터프레임의 조인을 수행, 등가조건만을 사용하여 조인 가능(equi join만 가능)

emp = pd.read_csv('emp.csv')
df_dept = DataFrame({'deptno':[10,20,30], 'dname':['인사부','총무부','재무부']})

pd.merge(left,           # 첫번째 데이터프레임
         right,          # 두번째 데이터프레임
         how='inner',    # 조인 방법
         on = ,          # 조인 컬럼(컬럼명이 서로 같을 때)  => 컬럼명이 여러개인 경우 리스트로 묶어서 전달
         left_on = ,     # 첫번재 데이터프레임 조인 컬럼(컬럼명이 서로 다를 때) => 컬럼명이 여러개인 경우 리스트로 묶어서 전달
         right_on = )    # 두번재 데이터프레임 조인 컬럼(컬럼명이 서로 다를 때) => 컬럼명이 여러개인 경우 리스트로 묶어서 전달
         

pd.merge(emp, df_dept, on = 'deptno')

# OUTER JOIN
df_dept = DataFrame({'deptno':[10,20], 'dname':['인사부','총무부']})
pd.merge(emp, df_dept, on = 'deptno')    # 30번 부서원이 생략됨
pd.merge(emp, df_dept, on = 'deptno', how = 'left')    # 30번 부서원이 생략됨



# [ 응용문제 ]
# delivery.csv 파일을 읽고 음식업종별 판매량이 가장 많은 시간대 확인

deli = pd.read_csv('delivery.csv', encoding='cp949')
deli2 = deli.groupby(by=['업종', '시간대'], as_index=False)['통화건수'].sum()  

# 1) groupby + merge
deli_max = deli2.groupby('업종')['통화건수'].max().reset_index()
pd.merge(deli2, deli_max)

# 2) groupby + transform
deli2.groupby('업종')['통화건수'].max()
deli2['MAX'] = deli2.groupby('업종')['통화건수'].transform('max')
deli2.loc[deli2['통화건수'] == deli2['MAX'], :]       # 조건색인으로 데이터 추출
deli2.query('통화건수 == MAX')


