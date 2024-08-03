# -*- coding: utf-8 -*-
run my_profile

# 연습 문제 : ex_test1.csv 파일을 읽고
df1 = pd.read_csv('ex_test1.csv', encoding='cp949')

# 1. 각 구매마다의 포인트를 확인하고 point 컬럼 생성
# point는 주문금액 50000 미만 1%, 5만 이상 10만 미만 2%, 10만 이상 3%
# 문제 풀이 포인트 : 조건에 따른 치환 혹은 연산

# sol1) for + if
result = []

for i in df1['주문금액'] :
    if i < 50000 :
        result.append(i * 0.01)
    elif i < 100000 :
        result.append(i * 0.02)
    else :
        result.append(i * 0.03)
        
df1['point'] = np.round(result,2)    

# sol2) np.where(벡터 연산 가능한 조건 연산 함수)
# np.where(조건, 참리턴, 거짓리턴)

np.where(df1['주문금액'] < 50000, df1['주문금액'] * 0.01, df1['주문금액'] * 0.02)
np.where(df1['주문금액'] < 50000,    # 첫번째 조건
         df1['주문금액'] * 0.01,     # 첫번째 조건이 참일 경우 연산 값
         np.where(df1['주문금액'] < 100000,   # 첫번째 조건이 거짓일 경우 또 다른 조건 추가
                  df1['주문금액'] * 0.02,     # 두번째 조건이 참일 경우 연산 값
                  df1['주문금액'] * 0.03))    # 두번째 조건이 거짓일 경우 연산 값


df1['point2'] = np.where(df1['주문금액'] < 50000, df1['주문금액'] * 0.01, np.where(df1['주문금액'] < 100000, df1['주문금액'] * 0.02, df1['주문금액'] * 0.03))


# 2. 회원번호별 총 주문금액과 총 포인트 금액 확인
df1.groupby('회원번호')[['주문금액', 'point']].sum()


# [ 연습 문제 - Y값을 서로 다른 숫자로 변경 ]
# 출제의도 : 조건에 따른 치환
df2 = DataFrame({'Y' : ['a','a','b','b','c','a','b','c'],
                 'X1' : [1,2,4,4,6,3,5,4],
                 'x2' : [10,30,43,34,43,43,94,32]})

# 하나씩 사용자가 치환
df2['Y'].replace({'a':0, 'b':1, 'c':2})

# 자동변환 함수
from sklearn.preprocessing import LabelEncoder

m_lb = LabelEncoder()
m_lb.fit_transform(df2['Y'])


# [ 연습 문제 - 조건에 따른 값의 수정 ]
# df2에서 X1이 5이상일 경우 X1 평균으로 수정(최빈값, 중앙값, 최솟값)
df2 = DataFrame({'Y' : ['a','a','b','b','c','a','b','c'],
                 'X1' : [1,2,4,4,6,3,5,4],
                 'x2' : [10,30,43,34,43,43,94,32]})

m1 = df2['X1'].mean()
m2 = df2['X1'].median()
m3 = df2['X1'].mode()           # Series로 리턴
m4 = df2['X1'].mode()[0]        # 하나의 상수로 리턴
m5 = df2['X1'].min() 
m6 = df2['X1'].max() 

import statistics as stat
stat.mode(df2['X1'])            # 하나의 상수로 리턴

df2.loc[df2['X1'] >= 5, 'X1'] = m3    # NA로 수정이 되고 있음(문제 발생)
df2.loc[df2['X1'] >= 5, 'X1'] = m4    # 정상




















