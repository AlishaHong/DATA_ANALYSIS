# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# 기타 메서드 
# 1. drop 
# - 특정 행, 컬럼 제거
# - 이름을 전달

# [ 예제 - emp 데이터에서 scott 행 제외 ]
emp = pd.read_csv('emp.csv')
emp.loc[~(emp['ename'] == 'scott'), : ]

emp = emp.drop(4, axis=0)

# [ 예제 - emp 데이터에서 sal 컬럼 제외 ]
emp.iloc[:,0:3]
emp.loc[:, 'empno':'deptno']
emp = emp.drop('sal', axis=1)

emp = emp.drop(['ename', 'deptno'], axis=1)


# 2. shift
# - 행이나 열을 이동
# - 전일자 대비 증감율 

emp = pd.read_csv('emp.csv')
emp['sal'].shift()

# [ 예제 - 다음의 데이터프레임에서 전일자 대비 증감율 출력 ]
s1 = Series([3000,3500,4200,2800, 3600], index = ['2021/01/01','2021/01/02','2021/01/03','2021/01/04','2021/01/05'])

# 1월 2일의 증감율 => (3500 - 3000) / 3000
(s1 - s1.shift()) / s1.shift() * 100

# 3. rename
# - 행이나 컬럼명 변경
emp.columns = ['empno', 'ename', 'deptno', 'salary']
emp = emp.rename({'salary' : 'sal', 'deptno': 'dept_no'}, axis=1)

# [ 예제 - emp 데이터에서 ename을 인덱스로 설정 후 scott => SCOTT 변경 ] 
emp = emp.set_index('ename')
emp = emp.rename({'scott':'SCOTT'}, axis=0)


# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame

# [ multi (level) index ]
# - 여러 depth(level)로 index 구성 
# - 각 level마다 이름을 전달하여 구분하거나 level 마다 번호를 부여(가장 상위 레벨이 0)

# 1. 생성
df1.index = [idx1, idx2] 
df1.set_index([idx1, idx2])
df1.column = [idx1, idx2] 

# 2. 각 level 이름 확인 및 부여
df1.index.name
df1.index.names = [name1, name2]

df1.columns.name
df1.columns.names = [name1, name2]

# 3. 색인
# - 상위 레벨일 경우 기존 색인 방식 사용
# - xs 메서드를 사용하여 하위 레벨로 접근 가능

# 예) 
import numpy as np
df1 = DataFrame(np.arange(1,17).reshape(4,4))
df1.index = [['서울','서울','경기','경기'], ['A','B','A','B']]
df1.columns = [['남','남','여','여'], [1,2,1,2]]

df1.index.names = ['지역','지점']
df1.columns.names = ['성별','학년']
df1.index.names = [None,None]         # 이름 삭제 시

df1['남']
df1.loc[:,'남']
df1.loc['서울',:]

df1.loc['A',:]               # loc 메서드로 하위레벨로 직접 접근 불가
df1.loc[('서울','A'),:]      # loc 메서드로 순서대로 접근 가능(튜플로 전달)

df1.xs('A', axis=0, level=1)                     # 레벨축소 발생
df1.xs('A', axis=0, level=1, drop_level=False)   # 레벨춗호 방지

# 4. 연산
df1.sum(axis=0, level=1)
df1.groupby(axis=0, level=1).sum()
df1.groupby(axis=0, level=1).sum().groupby(axis=1, level=0).sum()

# [ 연습문제 ] multi index 생성
df2 = pd.read_csv('multi_index_ex1.csv', encoding='cp949')

# -- index 설정
df2 = df2.set_index(['지역','지역.1'])
df2.index.names = ['대분류','소분류']

# -- column 설정
c1 = df2.columns.str[:2]
c2 = df2.iloc[0,:]
df2.columns = [c1, c2]
df2 = df2.drop('지점', axis=0, level=0)
df2.columns.names = ['지역','지점']

# -- 숫자컬럼 변경
df2.dtypes
df2 = df2.astype('int')

# -- 지점별 대분류별 매출 총 합
df2.groupby(axis=1, level=1).sum().groupby(axis=0, level=0).sum()
