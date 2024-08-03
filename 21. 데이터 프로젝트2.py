# -*- coding: utf-8 -*-
run my_profile

# card.csv 파일을 읽고
# 일자별 총 지출 금액을 구하여 마지막 컬럼에 추가
# (천단위 구분기호 제거 후 숫자 컬럼 변경******)
card = pd.read_csv('card.csv', encoding='cp949')
card = card.set_index('NUM')

# 천단위 구분기호 제거 후 숫자 컬럼 변경
int('19,400'.replace(',',''))                # 형변환 함수 사용하여 숫자로 변경
'19,400'.replace(',','').astype('int')       # 문자열에 사용 불가(array, Series, DataFrame에 사용 가능)

f1 = lambda x : int(x.replace(',','')) 
card = card.applymap(f1)                            # 2차원 데이터 셋(DataFrame)에 함수 적용을 위해 사용(applymap)

# 일자별 총 합
card['총합'] = card.sum(axis=1)


# [ 참고 - 위 함수를 특정 컬럼에 대해서 적용 ]
card = pd.read_csv('card.csv', encoding='cp949')
card = card.set_index('NUM')

f1 = lambda x : int(x.replace(',','')) 
card['식료품'].applymap(f1)                         # 1차원 데이터 셋(Series)에 적용 불가
card['식료품'] = card['식료품'].map(f1)              # 1차원 데이터 셋(Series)에 적용 불가

card['의복'] = card['의복'].str.replace(',','').astype('int')

card['책값'].replace(',','')                        # 값치환 메서드(특정 값과 정확히 일치하는 값을 변경, 삭제)
card['책값'].replace('28,000','')                   # 값치환 메서드(특정 값과 정확히 일치하는 값을 변경, 삭제)

# 2) 일자별로 각 품복별 지출 비율을 출력(%로)
card = pd.read_csv('card.csv', encoding='cp949')
card = card.set_index('NUM')

f1 = lambda x : int(x.replace(',','')) 
card = card.applymap(f1)

# 첫번째 행에 대해 확인
card.iloc[0,:].sum()     # 첫째날 지출 총 합
card.iloc[0,:] / card.iloc[0,:].sum() * 100

# apply 메서드를 사용하여 각 일자별로 적용
f2 = lambda x : x / x.sum() * 100
card.apply(f2, axis=1)



# 형변환 : 함수, astype 메서드
# 적용함수 : map 함수, map 메서드, apply 메서드, applymap 메서드
# 치환함수 : 문자열 메서드, 벡터화 내장된 문자열 메서드, 값치환 메서드
# 색인
# 컬럼추가, 컬럼 내용 변경

