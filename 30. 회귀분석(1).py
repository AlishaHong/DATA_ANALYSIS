# -*- coding: utf-8 -*-

# 1. data loading
from sklearn.datasets import load_boston
boston = load_boston()
boston_x = boston['data']
boston_y = boston['target']

# 2. data split
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(boston_x, boston_y, random_state=0)

# 3. modeling
from sklearn.linear_model import LinearRegression
m_lm = LinearRegression()
m_lm.fit(train_x, train_y)

# 4. score
m_lm.score(train_x, train_y)   # 76.97(R^2)
m_lm.score(test_x, test_y)     # 63.54(R^2)

# 5. 확인
dir(m_lm)        # 모델이 갖는 속성 정보 확인
m_lm.coef_       # 회귀 계수
m_lm.intercept_  # 회귀 절편


# 6. 변수간 상관관계 
# 1) 상관 계수
from pandas import Series, DataFrame
boston_corr = DataFrame(boston_x, columns = boston.feature_names).corr()

import seaborn as sb
sb.heatmap(boston_corr,      # 상관계수행렬 
           annot = True,     # 상관계수 출력 여부
           cmap = 'Reds')    # color mapping

# 2) VIF(VIF > 10이면 다중공선성 의심)
from statsmodels.stats.outliers_influence import variance_inflation_factor
variance_inflation_factor(boston_x,   # 설명변수 데이터 셋
                          0)          # VIF를 구할 target 설명변수 위치 값
variance_inflation_factor(boston_x,   # 설명변수 데이터 셋
                          9)          # VIF를 구할 target 설명변수 위치 값

boston.feature_names[9]
x1 = x2 + x3 + x4 + x5
x2 = x1 + x3 + x4 + x5


# 다중공선성의 문제 해결을 위한 모델링
# 1) PCA
from sklearn.decomposition import PCA
m_pca = PCA(10, whiten=True)
boston_x_pca = m_pca.fit_transform(boston_x)

m_lm2 = LinearRegression()
m_lm2.fit(boston_x_pca, boston_y)
m_lm2.score(boston_x_pca, boston_y)

boston['data'].shape


# 2) 릿지(Ridge) : L2규제 사용 => 가중치의 제곱의 합이 최소화 되는 방식
# (회귀 계수를 0에 가까운 값으로 규제)
from sklearn.linear_model import Ridge 

m_rg1 = Ridge()             # alpha : 1
m_rg2 = Ridge(alpha=10)     # alpha : 10(규제 강화 => 변수의 계수가 0에 가깝게 규제)
m_rg3 = Ridge(alpha=0.01)   # alpha : 0.01

m_rg1.fit(train_x, train_y)
m_rg2.fit(train_x, train_y)
m_rg3.fit(train_x, train_y)

m_rg1.score(test_x, test_y)   # 62.66
m_rg2.score(test_x, test_y)   # 61.32
m_rg3.score(test_x, test_y)   # 63.53

m_rg1.coef_
m_rg2.coef_
m_rg3.coef_

import matplotlib.pyplot as plt
plt.plot(m_rg1.coef_, 's', label = 'ridge alpha 1')
plt.plot(m_rg2.coef_, '^', label = 'ridge alpha 10')
plt.plot(m_rg3.coef_, 'v', label = 'ridge alpha 0.01')

plt.legend()

# 3) 라쏘(Lasso) : L1 규제 => 가중치의 절대값의 합이 최소화 되는 방식
# 회귀 계수를 0에 가까운 혹은 0으로 규제
# alpha가 클수록 규제 강화
from sklearn.linear_model import Lasso

m_ls1 = Lasso()                 # alpha : 1
m_ls2 = Lasso(alpha = 10)
m_ls3 = Lasso(alpha = 0.001)

m_ls1.fit(train_x, train_y)
m_ls2.fit(train_x, train_y)
m_ls3.fit(train_x, train_y)

m_ls1.score(test_x, test_y)
m_ls2.score(test_x, test_y)
m_ls3.score(test_x, test_y)

(m_ls1.coef_ == 0).sum()    # 2개 변수의 회귀 계수가 0
(m_ls2.coef_ == 0).sum()    # 9개 변수의 회귀 계수가 0
(m_ls3.coef_ == 0).sum()    # 0개 변수의 회귀 계수가 0

from sklearn.linear_model import ElasticNet
