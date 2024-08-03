# -*- coding: utf-8 -*-
# [ 변수 스케일링 ]
# scaling module
from sklearn.preprocessing import StandardScaler as standard
from sklearn.preprocessing import MinMaxScaler as minmax

# iris data loading
from sklearn.datasets import load_iris
iris_x = load_iris()['data']
iris_y = load_iris()['target']

# 1) standard scaling(표준화) : (x - xbar) / sigma
# 1-1) 직접 계산
(iris_x - iris_x.mean(axis=0)) / iris_x.std(axis=0)   # [ 6.86617933e-02, -1.31979479e-01,  7.62758269e-01, 7.90670654e-01]

# 1-2) 함수 사용
m_sc = standard()
m_sc.fit(iris_x)
m_sc.transform(iris_x)                                 # [ 6.86617933e-02, -1.31979479e-01,  7.62758269e-01, 7.90670654e-01]

# 2) minmax scaling : (x - x.min()) / (x.max() - x.min())
# 2-1) 직접 계산
df1 = (iris_x - iris_x.min(0)) / (iris_x.max(0) - iris_x.min(0))
df1.min()
df1.max()

# 2-2) 함수 사용
m_sc_mm = minmax()
m_sc_mm.fit(iris_x)
df2 = m_sc_mm.transform(iris_x)

df2.min()
df2.max()


# train/test로 분리되어진 데이터의 표준화
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y)

# 1) train_x, test_x을 동일한 기준으로 스케일링
m_sc1 = minmax()
m_sc1.fit(train_x)
train_x_sc1 = m_sc1.transform(train_x)
test_x_sc1 = m_sc1.transform(test_x)

train_x_sc1.min(0)
train_x_sc1.max(0)

test_x_sc1.min(0)   # 0이 아님
test_x_sc1.max(0)   # 1이 아님

# 2) train_x, test_x을 서로 다른 기준으로 스케일링
m_sc2 = minmax()
m_sc3 = minmax()

m_sc2.fit(train_x)
m_sc3.fit(test_x)

train_x_sc2 = m_sc2.transform(train_x)
test_x_sc2 = m_sc3.transform(test_x)

train_x_sc2.min(0)
train_x_sc2.max(0)

test_x_sc2.min(0)   
test_x_sc2.max(0)   


# [ scaling 시각화 ]
# 1) figure, subplot 생성
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,3)

# 2) 원본 data의 산점도
import mglearn

ax[0].scatter(train_x[:,0], train_x[:,1], c=mglearn.cm2(0), label='train')
ax[0].scatter(test_x[:,0], test_x[:,1], c=mglearn.cm2(1), label='test')
ax[0].legend()
ax[0].set_title('raw data')


# 3) 올바른 스케일링 data의 산점도(train_x_sc1, test_x_sc1)
ax[1].scatter(train_x_sc1[:,0], train_x_sc1[:,1], c=mglearn.cm2(0), label='train')
ax[1].scatter(test_x_sc1[:,0], test_x_sc1[:,1], c=mglearn.cm2(1), label='test')
ax[1].legend()
ax[1].set_title('good scaing data')


# 4) 잘못된 스케일링 data의 산점도(train_x_sc2, test_x_sc2)

ax[2].scatter(train_x_sc2[:,0], train_x_sc2[:,1], c=mglearn.cm2(0), label='train')
ax[2].scatter(test_x_sc2[:,0], test_x_sc2[:,1], c=mglearn.cm2(1), label='test')
ax[2].legend()
ax[2].set_title('bad scaling data')



