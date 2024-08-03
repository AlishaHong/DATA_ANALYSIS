# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 12:44:09 2024

@author: user
"""

import pandas as pd

#1. 병원현황 파일 불러오기
#2. 인코딩완료
#3. 첫 행 생략
#4. 모듈 호출 
hos = pd.read_csv('(과제 Data1_중간)병원현황.csv',encoding='cp949',skiprows = 1)
type(hos)
hos

hos.set_index(['시군구명칭','표시과목'])
hos_4 = hos[['시군구명칭', '표시과목', '항목', '단위', '2013. 4/4', '2012. 4/4', '2011. 4/4', '2010. 4/4', '2009. 4/4']]
hos_4.columns = ['시군구명칭', '표시과목', '항목', '단위', '2013', '2012', '2011', '2010', '2009']



pd.set_option('display.max_rows',100)


#표시과목이 계인 행 삭제하기
hos_4 = hos_4[~(hos['표시과목']=='계')]
hos_4.set_index(['시군구명칭','표시과목'])

#열 이름이 항목/단위 인 열 삭제
hos_4 = hos_4.drop(['항목','단위'],axis=1).set_index(['시군구명칭','표시과목'])

hos_4.groupby('표시과목').sum()
hos_4.groupby('시군구명칭')['표시과목'].sum()


#시군구명칭별 + 표시과목별 병원수의 총 합 
hos_4['합계'] = hos_4[['2013','2012','2011','2010','2009']].sum(axis=1)    #여기서의 축은 각기 다른 열끼리의 합(가로방향)


#시군구 명칭별 합계가 가장 큰 인덱스 출력
max_hos = hos_4.groupby(['시군구명칭'])['합계'].idxmax()
max_hos2 = hos_4.sort_values(by='합계', ascending=False).groupby('시군구명칭').head(1).index





 