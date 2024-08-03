# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series, DataFrame

emp = pd.read_csv('emp.csv')

# 정렬
# 1. sort_index
# - Series, DataFrame 호출 가능
# - index, column 재배치

emp = emp.set_index('empno')
emp.sort_index(ascending=False)            # index 내림차순 정렬
emp.sort_index(axis=1)                     # 컬럼 순서 정렬 재배치

# 2. sort_values
# - Series, DataFrame 호출 가능
# - 본문의 값으로 정렬 가능(시리즈 값 또는 데이터프레임 특정 컬럼 순서대로)

emp.sort_values(by='sal')                    # 오름차순 정렬(기본)
emp.sort_values(by='sal', ascending=False)   # 내림차순 정렬

emp.sort_values(by=['deptno', 'sal'], ascending=[True, False])

# [ 참고 - 인덱스 변경 ]
emp.index = emp['empno']
emp = emp.iloc[:,1:]

emp = pd.read_csv('emp.csv')
emp.set_index('empno')



# [ 순위 ]
# - rank 메서드 사용
# - 동순위 처리 방식에 따라 순위 결과 달라짐
#   예) 순서대로 2등과 3등이 동순위 처리 되어야 하는 경우
#       average => 2.5등
#       min => 2등
#       max => 3등
#       first => 각각 2,3등(먼저 오는 값을 우선 순위)
      
emp['rank'] = emp['sal'].rank(ascending=False)                 # method=average default
emp['rank'] = emp['sal'].rank(ascending=False, method='min')   # 5,6등 => 5등
emp['rank'] = emp['sal'].rank(ascending=False, method='max')   # 5,6등 => 6등
emp['rank'] = emp['sal'].rank(ascending=False, method='first') # 5,6등 => 5,6등


emp['rank_deptno'] = emp['deptno'].rank(method='dense')   
emp['rank_deptno'] = emp['deptno'].rank(method='min')     

emp.sort_values('deptno')


