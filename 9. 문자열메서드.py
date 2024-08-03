# -*- coding: utf-8 -*-

# 문자열 메서드
# 문자열 처리와 관련된 메서드

# 1. 기본 메서드 : 벡터연산 불가(매 원소마다 반복 불가)
'abc'.upper()
'a/b/c'.split('/')[1]

l1 = ['abc', 'def']
l2 = ['a/b/c', 'd/e/f']

l1.upper()             # 불가
l2.split('/')          # 불가

list(map(lambda x : x.upper(), l1))
list(map(lambda x : x.split('/')[1], l2))


# 2. pandas 메서드 : 벡터화 내장(매 원소마다 반복 가능)
# Series, DataFrame에 적용 가능
from pandas import Series, DataFrame

# 1) split
s1 = Series(l1)
s2 = Series(l2)

s2.str.split('/')

# 2) 대소치환
s1.str.upper()    # 대문자 치환
s1.str.lower()    # 소문자 치환
s1.str.title()    # 단어의 앞글자만 대문자 치환(나머지 소문자)

# 3) replace
s1.str.replace('a','A')  # 문자열 치환
s1.str.replace('a','')   # 문자열 삭제

# [ 예제 - 천단위 구분기호 처리 ]
s3 = Series(['1,200', '3,000', '4,000'])
s3.sum()   # 천단위 구분기호때문에 문자로 입력된 값이라 문자열의 결합으로 해석

s3.str.replace(',','').astype('int').sum()  # 정상 처리

# 4) 패턴확인 : startswith, endswith, contains
s1[s1.str.startswith('a')]    # s1 각 원소에서 'a'로 시작하는 원소 추출
s1[s1.str.endswith('c')]      # s1 각 원소에서 'c'로 끝나는는 원소 추출
s1[s1.str.contains('e')]      # s1 각 원소에서 'e'를 포함하는

# 5) len : 문자열 크기
s1.str.len()                  # 각 원소의 크기

# 6) count : 포함 개수
Series(['aabab', 'abcda']).str.count('a')

# 7) 제거 함수(공백, 문자)
Series(['   cd   ', '   df   ']).str.strip()             # 기본적으로 공백 제거
Series(['   cd   ', '   df   ']).str.strip().str.len()

s1.str.strip('a')   # 문자열 제거
Series(['aaabaaca','abcda']).str.strip('a')          # 문자열 제거(중간값 삭제 불가)
Series(['aaabaaca','abcda']).str.replace('a', '')    # 문자열 제거(중간값 삭제 가능)

# 8) find : 위치값 리턴
s3 = Series(['abc@abc.com', 'abcde@abc.com']) 
s3.str.find('@')

# 9) 문자열 색인(추출)
'abcde'[0:3]   # 문자열 색인
s3[0:3]        # Series에서 첫번째 두번째 세번째 원소 추출

s3.str[0:3]    # Series에서 각 원소마다 첫번째에서 세번째까지의 문자열 추출

# [ 예제 - 이메일 아이디 추출 ]
s3 = Series(['abc@abc.com', 'abcde@abc.com']) 
vno = s3.str.find('@')
s3.str[0:3]

list(map(lambda x,y : x[0:y], s3, vno))

# 10) pad : 문자열 삽입
s1.str.pad(5,        # 총자리수
           'left',   # 삽입 방향
           '!')      # 삽입 글자

# 11) 문자열 결합
'a' + 'b'
'a' * 3

s4 = Series(['abc','def','123'])
s4.str.cat()            # 시리즈 내 서로 다른 원소를 결합
s4.str.cat(sep='/')     # 시리즈 내 서로 다른 원소를 결합(분리구분기호와 함께)

s5 = Series([['a','b','c'], ['d','e','f']])
s5.str.join(sep='')           # 시리즈 내 각 원소 내부의 문자열을 결합
s5.str.join(sep=',')          # 시리즈 내 각 원소 내부의 문자열을 결합
