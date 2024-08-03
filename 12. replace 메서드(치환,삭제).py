# -*- coding: utf-8 -*-

# replace 메서드
# 치환(찾을 문자열, 바꿀문자열)

# 1. 기본 문자열 메서드
# - 기본 파이썬 제공
# - 문자열에서 호출 가능
# - 벡터연산(각 원소별 반복 처리) 불가
# - 오로지 문자열 치환만 가능(숫자 치환, NA 치환 불가)
'abcd'.replace('a', 'A')   # a를 A로 치환
'abcd'.replace('a', '')    # a를 삭제
'abcd1'.replace(1, '')     # 숫자를 찾아서 치환 불가
'abcd1'.replace('a', 1)    # 숫자로 치환 불가


['abcd','abcde','aaab'].replace(',', '')    # 'list' object has no attribute 'replace'

# --
outlist = []
for i in ['abcd','abcde','aaab'] :
    outlist.append(i.replace('a','A'))

# -- 
f1 = lambda x : x.replace('a','A')
list(map(f1, ['abcd','abcde','aaab']))

# -- 
from pandas import Series, DataFrame
['abcd','abcde','aaab'].map(f1)    # 호출 불가
Series(['abcd','abcde','aaab']).map(f1)    # 호출 불가

from numpy import nan as NA
Series(['abcd','abcde','aaab', NA]).map(lambda x : x.replace(NA,''))   # NA치환 불가


# 2. str.replace
# - pandas 제공(Series 객체만 호출 가능)
# - 벡터화 내장된 문자열 메서드
# - 숫자로 구성된 Series에 적용 불가
# - 벡터연산(각 원소별 반복 처리) 가능
# - 오로지 문자열 치환만 가능(숫자 치환, NA 치환 불가)

Series(['abcd','abcde','aaab']).str.replace('a','A')
['abcd','abcde','aaab'].str.replace('a','A')              # 리스트 호출 불가
DataFrame(['abcd','abcde','aaab']).str.replace('a','A')   # 데이터프레임 호출 불가


# 3. pandas replace
# - pandas 제공
# - 값 치환 메서드(똑같은, 완전히 일치하는 값을 다른 값으로 대치/삭제)
# - Series, DataFrame 호출 가능
# - 숫자, NA 치환도 가능
# - 동시에 여러 대상을 수정할 수 있음
df1 = DataFrame([['1,200','1,200'],['1,400','1,500']])
df2 = DataFrame([['1,200',','],['1,400','1,500']])

df1.replace(',','')        # 변화 없음, ','로 생긴 값을 삭제하라는 의미
df2.replace(',','')


df3 = DataFrame([[1200,1300],[1400,'.']], columns = ['a','b'])
df3.replace('.', NA)                # '.'과 일치하는 값을 NA로 수정
df3.replace(['.',1400,'?'], NA)     # 다수 대상에 대한 치환 가능


# [ 연습 문제 ]
# df1에서 천단위 구분기호 제거 후 모두 숫자 변경
df1.replace(',','')
df1.str.replace(',','')

df1.applymap(lambda x : int(x.replace(',','')))


# [ 응용문제 ] 
df1 = pd.read_csv('apply_test2.csv', encoding='cp949')

# 1) 특수기호들을 모두 NA로 치환
df1.iloc[1,2]                                 # 특수기호 앞뒤 공백 삽입 확인
df1.replace(['-','.','?'], NA)                # 치환 발생 X
df1 = df1.applymap(lambda x : x.strip())
df1 = df1.replace(['-','.','?'], NA)          # 치환 가능

# 2) 지점별 매출 평균
df1 = df1.set_index('name')
df1 = df1.applymap(lambda x : float(str(x).replace(',','')))
df1.mean(axis=1)




