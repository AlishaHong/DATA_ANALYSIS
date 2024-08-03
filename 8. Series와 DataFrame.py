# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series, DataFrame

# pandas : 2차원 정형데이터(테이블, 표, 데이터프레임)
# Series 
# 1차원 자료 구조
# 하나의 데이터 타입 허용

# 1. 생성
s1 = Series([1,2,3,4])
s2 = Series([1,2,3,'4'])

s3 = Series([1,2,3,4], index = ['a', 'b', 'c', 'd'])
Series(s3, index = ['A','B','C','D'])  # 이미 index가 존재하는 경우
                                       # Series의 index 옵션은 해당 값대로 재배치!
                                       
# 2. 색인
s1[0]       # 차원 축소 O(Scalar로 리턴)
s1[0:1]     # 차원 축소 X(Series로 리턴)
s1[[0,3]]   # 차원 축소 X(Series로 리턴)

s3['a']
s3[['a','c']]
s3['a':'c']     # 문자의 연속 추출은 마지막 범위 포함(a~c)

s1[s1 > 2]

s3.a            # key indexing

# 3. 연산
s1 + 1

s4 = Series([10,20,30,40])
s5 = Series([10,20,30,40], index = ['c','d','e','f'])
s1 + s4   # key가 같은 값끼리 연산 가능
s3 + s5   # key가 다른 경우 모두 NA리턴
s3.add(s5, fill_value=0)    # 양쪽 모두 존재하지 않는 key일 경우
                            # NA가 리턴되는 것 방지(fill_value옵션)
s3.sub(s5, fill_value=0)    # - 연산
s3.mul(s5, fill_value=1)    # * 연산
s3.div(s5, fill_value=1)    # / 연산

# 4. 기본 메서드
s1.dtype     # 데이터 타입 출력
s1.index     # index 출력
s3.index     # index 출력
s1.values    # 값 출력

s3[['c','d','a','b']]            # 색인을 사용하여 배치 순서 변경 가능             
s3.reindex(['c','d','a','b'])    # 메서드로 배치 순서 변경 가능                     

s3.index = ['A','B','C','D']     # index 수정
s3[0] = 10                       # 값 수정 가능


# DataFrame
# 2차원 자료 구조(행과 열의 구조)
# 1. 생성
d1 = {'name' : ['smith', 'allen'], 'sal' : [900,800]}
DataFrame(d1)
d2 = DataFrame({'name' : ['smith', 'allen'], 'sal' : [900,800]})

import numpy as np
d3 = DataFrame(np.arange(1,7).reshape(2,3), index = ['a','b'], columns = ['col1','col2','col3'])

# 2. 색인****
d3['col1']   # 컬럼 선택
d3.col1      # 컬럼 선택

# [행방향,컬럼방향]
d3.iloc[:,0]                 # positional indexing
d3.iloc[:,0:3]     
d3.iloc[:,[0,2]]   
d3.iloc[1,1]      

d3.loc[:,['col1','col3']]    # label indexing  

d3.loc[d3.col1 == 1, :]      # 조건 색인 처리

# 3. 기본 메서드
d3.dtypes   # 각 컬럼별 데이터 타입 확인
d3.index    # index
d3.columns  # column
d3.values

d3.columns = ['A','B','C']   # column 이름 변경

# 4. 연산
d3 + 10

d4 = DataFrame({'A':[10,40], 'B':[20,30], 'C':[30,60]}, index = ['a','b'])
d5 = DataFrame({'A':[10,40], 'B':[20,30]}, index = ['a','b'])

d3 + d5                   # 한쪽에만 있는 컬럼은 NA리턴
d3.add(d5, fill_value=0)  # 한쪽에만 있는 컬럼도 NA리턴 방지(원래값 유지)


