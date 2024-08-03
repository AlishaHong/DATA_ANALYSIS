# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series, DataFrame

# 적용 함수
# 함수에 데이터들의 일부를 전달하여 함수의 적용이 반복되도록 도와주는 함수(메서드)

df1 = DataFrame([['1,200', '1,300'],['1,400','1,500']], columns = ['A','B'])
df1.dtypes
df1['A'].sum()    # '1,200' + '1,400' : 문자열 결합으로 해석


df1['A'].str.replace(',','')    # 컬럼의 각 값에 replace를 전달하여 반복 연산 처리

df1.str.replace(',','')         # 'DataFrame' object has no attribute 'str'  

# 1. applymap
# - DataFrame 객체에서 호출 가능
# - 2차원 데이터의 각 원소별 함수 적용
# - 추가 객체, 함수의 추가 옵션 전달 불가

f1 = lambda x : int(x.replace(',',''))       # 문자열 메서드
df1 = df1.applymap(f1)                       # 2차원 데이터프레임의 각 원소별 함수 적용
df1.dtypes


# [ 참고 : replace 메서드 종류 ]
'1,200'.str.replace(',','')    # 불가(문자열은 str 메서드를 호출 불가)
'1,200'.replace(',','')        # 가능(문자열은 문자열 메서드를 호출 가능)

'a/b/c'.split('/')                             # 벡터화 내장되지 않은 문자열 메서드(문자열에서 호출 가능)
Series(['a/b/c', 'A/B/C']).str.split('/')      # 벡터화 내장된 문자열 메서드(시리즈에서 호출 가능)

# 2. map 메서드
# - 시리즈에서 호출 가능
# - 매 원소별 함수 적용
# - 추가 객체, 함수의 추가 옵션 전달 불가

f2 = lambda x : x.split('/')[0]
Series(['a/b/c', 'A/B/C']).map(f2)             # 시리즈 각각의 원소를 함수에 적용


# 3. apply
# - DataFrame 호출 가능
# - 각 행별, 컬럼별 적용 가능
# - 함수의 추가 옵션 전달 가능
df1.sum(axis=0)    # 행별 총 합(서로 다른 행끼리 총 합, 세로방향으로 총 합)
df1.sum(axis=1)    # 컬럼별 총 합(서로 다른 컬럼끼리 총 합, 가로방향으로 총 합)

df1.apply(sum, axis=0)    # 행별 총 합
df1.apply(sum, axis=1)    # 컬럼별 총 합

# [ 참고 : map 함수와 map 메서드 차이 ]
# map(함수, 1차원 자료구조(list, array, Series))
# 시리즈객체.map(함수)


# [ 연습 문제 ]
# apply.csv 파일을 읽고
df1 = pd.read_csv('apply.csv', encoding='cp949')

# 1) date 컬럼 생성(2019/05/01)
df1['month'] = df1['month'].map(lambda x : '%02d' % x)
df1['day'] = df1['day'].map(lambda x : '%02d' % x)

df1['date'] = df1['year'].astype('str') + '/' + df1['month'] + '/' + df1['day']

df1.iloc[:, [0,1,2,-1, -3, -2]]     # 컬럼 순서 재배치

# 2) id, passwd 분리, id/passwd 컬럼 삭제**
df1['id'] = df1['id/passwd'].map(lambda x : x.split('/')[0])
df1['passwd'] = df1['id/passwd'].map(lambda x : x.split('/')[1])     # out of range

'abc/123'.split('/')[1]
'abc'.split('/')[1]

# sol1) 강제로 /를 추가하여 split 진행
('abc' + '/').split('/')[1]
df1['passwd'] = df1['id/passwd'].map(lambda x : (x + '/').split('/')[1])     # 정상

# sol2) if + map
# lambda input_value : true_return if condition else false_return

f1 = lambda x : x.split('/')[1] if '/' in x else ''
df1['id/passwd'].map(f1)




