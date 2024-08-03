# -*- coding: utf-8 -*-

import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(1,17).reshape(4,4))

dir(df1)    # 데이터프레임 적용 가능한 메서드 목록 확인!!

df1.sum(axis=0)    # 행별(서로 다른 행끼리, 세로방향)
df1.sum(axis=1)    # 컬럼별(서로 다른 컬럼끼리, 가로방향)

df1.iloc[:,0].sum()
df1.iloc[:,0].mean()


df1.iloc[0,0] = np.nan
df1.iloc[:,0].mean()     # skipna = True가 기본이므로 자동으로 NA를 무시하고 연산

# NA값을 NA를 제외한 평균값(최대 혹은 최소)으로 대치
df1.iloc[:,0][df1.iloc[:,0].isnull()] = df1.iloc[:,0].mean()

df1[df1.isnull()]                    # 데이터프레임 전체에서 NA인 값 확인

df1.iloc[:,0].var()      # 분산
df1.iloc[:,0].std()      # 표준편차
df1.iloc[:,0].min()      # 최소
df1.iloc[:,0].max()      # 최대
df1.iloc[:,0].median()   # 중앙값

(df1.iloc[:,0] >= 10).sum()   # 조건에 만족하는 개수 확인


[ group by ]
# 그룹연산
# 성별 성적 평균, 학년별 성적 최고점수, 부서별 평균 연봉
# groupby 메서드로 처리 가능

kimchi = pd.read_csv('kimchi_test.csv', encoding='cp949')
kimchi.groupby(by,       # 그룹핑 컬럼
               axis=0,   # 그룹연산 방향
               level)    # 멀티 인덱스일 경우 특정 레벨의 값을 그룹핑 컬럼처럼 사용  
               
# 예제) 제품별(김치별) 수량 총 합
kimchi.groupby(by='제품').sum()            # 제품 컬럼 제외한 연산 가능한 모든 컬럼에 대해 그룹 연산 수행
kimchi.groupby(by='제품')['수량'].sum()     # 원하는 컬럼 전달
kimchi.groupby(by='제품')[['수량','판매금액']].sum()     # 원하는 컬럼 전달


# 예제) 제품별, 판매처 별(김치별) 수량 총 합
kimchi2 = kimchi.groupby(by=['제품','판매처'])['수량'].sum()     # 원하는 컬럼 전달

# 예제) 제품별, 판매처 별(김치별) 수량 총 합, 평균
kimchi.groupby(by=['제품','판매처'])['수량'].agg(['sum','mean'])              # 여러 함수를 동시에 전달

# 예제) 제품별, 판매처 별(김치별) 수량, 판매금액 총 합, 평균
kimchi3 = kimchi.groupby(by=['제품','판매처'])[['수량','판매금액']].agg(['sum','mean'])  # 여러 함수를 동시에 전달

# 예제) 제품별, 판매처 별(김치별) 수량의 총 합, 판매금액 평균
kimchi.groupby(by=['제품','판매처'])[['수량','판매금액']].agg({'수량':'sum','판매금액':'mean'})  # 각 컬럼에 서로 다른 함수 적용

# 멀티 레벨을 갖는 경우의 groupby 연산
type(kimchi2)
kimchi2.groupby(level=0).sum()    # 제품별 총 합
kimchi2.groupby(level=1).sum()    # 판매처별 총 합

kimchi3.groupby(axis=1, level=1).sum()


** groupby 추가 옵션
kimchi.groupby(by='제품', as_index=False)['수량'].sum()     # groupby 컬럼을 index로 배치하지X
                                                           # 출력 결과 데이터프레임 리턴 
                                                           
kimchi.groupby(by='제품')['수량'].sum().reset_index()

# [ 문제 ] 
# delivery.csv 파일을 읽고 음식 업종별 시간대별 통화건수 총 합
deli = pd.read_csv('delivery.csv', encoding='cp949')
deli.groupby(['업종','시간대'])['통화건수'].sum()


