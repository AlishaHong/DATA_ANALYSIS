# -*- coding: utf-8 -*-

# PCA 기법
# data loading
from sklearn.datasets import load_iris
iris_x = load_iris()['data']
iris_y = load_iris()['target']

# 2차원으로 축소
from sklearn.preprocessing import StandardScaler as standard
m_sc = standard()
iris_x_sc = m_sc.fit_transform(iris_x)   # PCA 적용 전 스케일링 변환

from sklearn.decomposition import PCA
m_pca2 = PCA(n_components=2)

iris_x_pca2 = m_pca2.fit_transform(iris_x_sc)


# 유도된 인공변수로 시각화
import mglearn
mglearn.discrete_scatter(iris_x_pca2[:,0], iris_x_pca2[:,1], y = iris_y)

# 3차원으로 축소
from sklearn.decomposition import PCA
m_pca3 = PCA(n_components=3)

iris_x_pca3 = m_pca3.fit_transform(iris_x_sc)

# 유도된 인공변수로 시각화
from mpl_toolkits.mplot3d import Axes3D, axes3d
import matplotlib.pyplot as plt

fig1 = plt.figure()
ax = Axes3D(fig1)

# step1) y == 0인 데이터포인트만 시각화
ax.scatter(iris_x_pca3[iris_y == 0, 0],   # X축 좌표   
           iris_x_pca3[iris_y == 0, 1],   # Y축 좌표
           iris_x_pca3[iris_y == 0, 2],   # Z축 좌표
           c='b',                               
           cmap=mglearn.cm2,          
           s=60,                                  
           edgecolors='k')                    

# step2) y == 1인 데이터포인트만 시각화
ax.scatter(iris_x_sc_pca3[iris_y == 1, 0],   # X축 좌표   
           iris_x_sc_pca3[iris_y == 1, 1],   # Y축 좌표
           iris_x_sc_pca3[iris_y == 1, 2],   # Z축 좌표
           c='r',                              
           cmap=mglearn.cm2,                    
           s=60,                               
           edgecolors='k')                      

# step3) y == 2인 데이터포인트만 시각화
ax.scatter(iris_x_sc_pca3[iris_y == 2, 0],   # X축 좌표   
           iris_x_sc_pca3[iris_y == 2, 1],   # Y축 좌표
           iris_x_sc_pca3[iris_y == 2, 2],   # Z축 좌표
           c='y',                              
           cmap=mglearn.cm2,                    
           s=60,                               
           edgecolors='k') 


# 모델 적용 ******
from sklearn.neighbors import KNeighborsClassifier as knn
m_knn1 = knn()
m_knn2 = knn()

from sklearn.model_selection import train_test_split
train_x1, test_x1, train_y1, test_y1 = train_test_split(iris_x_pca2, iris_y)
train_x2, test_x2, train_y2, test_y2 = train_test_split(iris_x_pca3, iris_y)

m_knn1.fit(train_x1, train_y1)
m_knn1.score(test_x1, test_y1)          # 94.74

m_pca2.explained_variance_ratio_        # 각 인공변수의 분산 설명력
sum(m_pca2.explained_variance_ratio_)   # 95.81% 설명력

m_knn2.fit(train_x2, train_y2)
m_knn2.score(test_x2, test_y2)          # 97.36

m_pca3.explained_variance_ratio_        # 각 인공변수의 분산 설명력
sum(m_pca3.explained_variance_ratio_)   # 99.48% 설명력


# MDS 기법에 의한 차원 축소
from sklearn.manifold import MDS
m_mds2 = MDS(n_components=2)
m_mds3 = MDS(n_components=3)

# 데이터 변환
iris_x_mds1 = m_mds2.fit_transform(iris_x_sc)
iris_x_mds2 = m_mds3.fit_transform(iris_x_sc)

# 유도된 인공 변수확인

m_mds2.stress_
points = m_mds2.embedding_    # 변환된 데이터 셋 값

# 크루스칼 스트레스 계산
import numpy as np
from sklearn.metrics import euclidean_distances
DE = euclidean_distances(points)
DA = euclidean_distances(iris_x)

stress = 0.5 * np.sum((DE - DA)**2)
stress1 = np.sqrt(stress / (0.5 * np.sum(DA**2)))


points = m_mds3.embedding_
DE = euclidean_distances(points)
DA = euclidean_distances(iris_x)

stress = 0.5 * np.sum((DE - DA)**2)
stress1 = np.sqrt(stress / (0.5 * np.sum(DA**2)))
