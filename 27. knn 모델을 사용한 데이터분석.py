# -*- coding: utf-8 -*-

# DATA SET LOADING(IRIS DATA)
from sklearn.datasets import load_iris
data_iris = load_iris()

data_iris.keys()
data_iris.data    # 150 X 4(array)
data_iris.feature_names 
data_iris.target
data_iris.target_names


# step1) 데이터 분리(train,test)
from sklearn.model_selection import train_test_split
train_test_split(X,                 # 설명변수 데이터 셋
                 y,                 # target 데이터 셋
                 train_size,        # train data 비중
                 test_size,         # test data 비중
                 random_state = 0)  # 랜덤 추출 데이터 고정     

train_x, test_x, train_y, test_y = train_test_split(data_iris.data, data_iris.target, random_state = 0)

# step2) 모델링
from sklearn.neighbors import KNeighborsClassifier as knn
import sklearn.neighbors
dir(sklearn.neighbors)

m_knn = knn()
m_knn.fit(train_x, train_y)
m_knn.predict(test_x)         # 예측값
m_knn.score(test_x, test_y)   # 예측점수

# step3) 튜닝
vscore_tr = [] ; vscore_te = []

for i in range(1,11) :
    m_knn = knn(n_neighbors=i)
    m_knn.fit(train_x, train_y)
    vscore_tr.append(m_knn.score(train_x, train_y))
    vscore_te.append(m_knn.score(test_x, test_y))   

import matplotlib.pyplot as plt
plt.plot(range(1,11), vscore_tr, label='train')
plt.plot(range(1,11), vscore_te, label='test')
plt.legend()

