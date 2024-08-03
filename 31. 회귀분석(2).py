# -*- coding: utf-8 -*-

# 회귀 분석
# 1. data loading
from sklearn.datasets import load_boston
boston = load_boston()
boston_x = boston['data']
boston_y = boston['target']

# 2. data split
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(boston_x, boston_y, random_state=0)

# 3. modeling
# 1) sklearn
from sklearn.linear_model import LinearRegression
m_lm = LinearRegression()
m_lm.fit(train_x, train_y)
m_lm.score(test_x, test_y)     # 63.54

m_lm.predict(test_x[0:1,:])    # 예측값(24.95)
test_y[0]                      # 실제값(22.6)

# 회귀분석표(유의성검정)
from regressors import stats  # pip install regressors 설치 필요!!

stats.summary(m_lm, train_x, train_y)


# 2) statmodels => 유의성 검정 가능
from statsmodels.formula.api import ols

# 데이터셋을 데이터프레임 형태로 변환
from pandas import Series, DataFrame
import pandas as pd

df1 = DataFrame(train_x, columns= boston.feature_names)
df2 = DataFrame(train_y.reshape(-1,1), columns = ['PRICE'])

df_train = pd.concat([df1,df2], axis = 1)

df3 = DataFrame(test_x, columns= boston.feature_names)
df4 = DataFrame(test_y.reshape(-1,1), columns = ['PRICE'])

df_test = pd.concat([df3,df4], axis = 1)

vfor = 'PRICE ~ ' + '+'.join(boston.feature_names)
m2 = ols(vfor, data = df_train).fit() # ols(Y ~ X1 + X2 + .... + , data = dataset)

m2.resid                # 잔차 
print(m2.summary())     # 회귀분석표(회귀계수, 모델에 대한 적합성 검정)


# 3) RandomForest 
from sklearn.ensemble import RandomForestRegressor
m3 = RandomForestRegressor()
m3.fit(train_x, train_y)
m3.score(test_x, test_y)     # 78.83
m3.predict(test_x[0:1,])     # 23.973


m3.feature_importances_

# 4) SVM(SVR)
from sklearn.svm import SVR
m4 = SVR()
m4.fit(train_x, train_y)
m4.score(test_x, test_y)     # 83.69
m4.predict(test_x[0:1,])     # 20.45

test_y[0]                    # 22.6


# 회귀분석 시 확인 할 기본 가정
# 1) 등분산성 : 잔차산점도로 확인
m2.fittedvalues   # 예측값
m2.resid          # 잔차

import matplotlib.pyplot as plt
plt.scatter(m2.fittedvalues , m2.resid)

# 2) 정규성 : 잔차의 정규성 확인 => 히스토그램, 커널밀도함수, qqplot, 샤피로검정
from scipy import stats
stats.probplot(m2.resid, plot = plt)

# 3) 선형성 : 독립변수와 종속변수간의 일정 패턴 존재 => 산점도
pd.plotting.scatter_matrix(df_train, hist_kwds = {'bins':20})

# 4) 잔차 자기상관성 : 잔차산점도, Durbin watson test
plt.scatter(m2.fittedvalues , m2.resid)

print(m2.summary())      #  Durbin-Watson:                   2.025

from statsmodels.stats.stattools import durbin_watson
durbin_watson(m2.resid)                                     # 2.025

# 0 ~ 4 값을 갖고, 0과 4에 가까울수록 자기상관이 강하다
#                 2에 가까울수록 자기상관이 없다(정확한 진단은 durbin watson table로 확인(n(훈련데이터 수),p(설명변수 수)에 따라 달라짐))

test_y - m3.predict(test_x)    # 잔차
