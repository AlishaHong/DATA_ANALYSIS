# -*- coding: utf-8 -*-

# 1. data loading
from sklearn.datasets import load_iris
iris = load_iris()
iris_x = iris.data
iris_y = iris.target

# 2. data split
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y, random_state=0)

# 3. modeling
# 1) LinearSVC
from sklearn.svm import LinearSVC
m1 = LinearSVC()
m1.fit(train_x, train_y)
m1.score(test_x, test_y)          # 92.10

# 2) SVM
from sklearn.svm import SVC
m1 = SVC(C=1)
m1.fit(train_x, train_y)
m1.score(test_x, test_y)          # 97.36

# 4. tunning
# 1) C : 규제 매개변수, 데이테포인트의 중요도 제한, 클수록 복잡한 경계 생성
vscore_tr = [] ; vscore_te = []
for i in [0.001, 0.01, 0.1, 1, 10, 100] :
    m1 = SVC(C=i)
    m1.fit(train_x, train_y)
    vscore_tr.append(m1.score(train_x, train_y))
    vscore_te.append(m1.score(test_x, test_y))

plt.plot([0.001, 0.01, 0.1, 1, 10, 100] , vscore_tr, c='r', label='train')
plt.plot([0.001, 0.01, 0.1, 1, 10, 100] , vscore_te, c='b', label='test')
plt.legend()

# 2) gamma : 커널 폭의 역수, 훈련 샘플이 미치는 영향의 범위를 결정, 클수록 복합한 경계 생성
    
    
# [ 시각화 ]
# 1. data loading
from sklearn.datasets import make_blobs
data_x, data_y = make_blobs(centers=4, random_state=8)
data_y  = data_y  % 2

# 2. data 분포 확인
import mglearn
import matplotlib.pyplot as plt

mglearn.discrete_scatter(data_x[:, 0], data_x[:, 1], data_y)
plt.xlabel("x1")
plt.ylabel("x2")

# 3. 2차원 데이터 셋의 선형 분류기 SVM을 통해 유도
from sklearn.svm import LinearSVC
m_svm = LinearSVC().fit(data_x, data_y)

mglearn.plots.plot_2d_separator(m_svm, data_x)    # 선형 분류기가 그려짐


# 4. 설명변수 추가(두 번째 설명변수의 제곱항) => 차원 확장
import numpy as np
data_x_new = np.hstack([data_x, data_x[:, 1:] ** 2])

# 5. 3차원 시각화
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(data_x_new[data_y==0, 0], data_x_new[data_y==0, 1], data_x_new[data_y==0, 2], c='b',
           cmap=mglearn.cm2, s=60, edgecolor='k')
ax.scatter(data_x_new[data_y==1, 0], data_x_new[data_y==1, 1], data_x_new[data_y==1, 2], c='r', marker='^',
           cmap=mglearn.cm2, s=60, edgecolor='k')
ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("x2 ** 2")

# 6. SVM 적용
m_svc2 = LinearSVC().fit(data_x_new, data_y)
coef = m_svc2.coef_.ravel()     
intercept  = m_svc2.intercept_

# 7. 초평면 시각화
from mpl_toolkits.mplot3d import Axes3D, axes3d
figure = plt.figure()
ax = Axes3D(figure)
xx = np.linspace(data_x_new[:, 0].min() - 2, data_x_new[:, 0].max() + 2, 50)    # 구간값 구하기  np.linspace(start,stop,num)
yy = np.linspace(data_x_new[:, 1].min() - 2, data_x_new[:, 1].max() + 2, 50)

XX, YY = np.meshgrid(xx, yy)   

ZZ = (coef[0] * XX + coef[1] * YY + intercept) / -coef[2]      

ax.plot_surface(XX, YY, ZZ, rstride=8, cstride=8, alpha=0.3)  
ax.scatter(data_x_new[data_y==0, 0], data_x_new[data_y==0, 1], data_x_new[data_y==0, 2], c='b',
           cmap=mglearn.cm2, s=60, edgecolor='k')
ax.scatter(data_x_new[data_y==1, 0], data_x_new[data_y==1, 1], data_x_new[data_y==1, 2], c='r', marker='^',
           cmap=mglearn.cm2, s=60, edgecolor='k')

ax.set_xlabel("x1")
ax.set_ylabel("x2")
ax.set_zlabel("x2 ** 2")
   
