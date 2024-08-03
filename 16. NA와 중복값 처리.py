# -*- coding: utf-8 -*-

# NA(결측치) 처리
# 숫자형 NA(float type), 문자형 NA
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

from numpy import nan as NA

s1 = Series([1,2,3,NA])
s2 = Series(['a','b','c',NA])

# 1. NA 수정
s1.fillna(0)          # fillna를 사용한 치환
s2.replace(NA, 'a')   # 값치환 메서드를 사용한 NA 치환 가능
s1[s1.isnull()] = 0   # 조건 색인을 통한 NA 처리 가능

# 2. NA로의 수정
s3 = Series(['서울','.','부산','.'])
s3 = s3.replace('.', NA)           # .을 NA로 수정

# 3. NA를 이전값/이후값으로 수정
s3.fillna(method='ffill')          # NA를 앞에 있는 값으로 치환
s3.ffill()                         # NA를 앞에 있는 값으로 치환

# 4. NA를 갖는 행, 컬럼 제거
df1 = DataFrame(np.arange(1,17).reshape(4,4), columns = list('ABCD'))

df1.iloc[0,0] = NA
df1.iloc[1,[0,1]] = NA
df1.iloc[2,[0,1,2]] = NA
df1.iloc[3,:] = NA

df1.dropna()             # NA를 하나라도 포함한 행을 제거
df1.dropna(how='any')    # NA를 하나라도 포함한 행을 제거
df1.dropna(how='all')    # 모든 값이 NA인 행을 제거

df1.dropna(thresh=2)           # NA가 아닌 값이 최소 2개 이상 있으면 제거하지 X
df1.dropna(axis=1, how='all')  # 특정 컬럼이 모두 NA로만 구성되어 있을 경우 해당 컬럼 제거

df1.dropna(subset=['C'])       # C 컬럼에 NA가 있는 행 제거



# 중복값 처리
s1 = Series([1,1,2,3,4])
s1.unique()             # 유일값 확인

s1.duplicated()         # 중복 여부 확인
s1.drop_duplicates()    # 중복 제거

df2 = DataFrame({'A':[1,1,3,4], 'B':[10,10,30,40]})
df2.drop_duplicates()

df3 = DataFrame({'A':[1,1,3,4], 'B':[10,10,30,40], 'C':[100,200,300,400]})
df3.drop_duplicates()                                    # 모든 컬럼의 값이 일치하는 행을 제거
df3.drop_duplicates(subset=['A','B'])                    # A와 B컬럼의 값이 일치하는 행 제거 
df3.drop_duplicates(subset=['A','B'], keep='last')       # 중복행 제거시 남길 행을 선택(first가 기본값)
