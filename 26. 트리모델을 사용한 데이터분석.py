# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 18:53:08 2021

@author: Hong
"""

# DATA LOADING
from sklearn.datasets import load_iris
data_iris = load_iris()

# step1) 데이터 분리
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(data_iris['data'], data_iris['target'], random_state=0)

# step2) modeling
from sklearn.tree import DecisionTreeClassifier as dt
m_dt = dt()
m_dt.fit(train_x, train_y)   # 학습용 데이터로 훈련
m_dt.score(test_x, test_y)   # 97.37%

# step3) 모델확인
dir(m_dt)

m_dt.feature_importances_
data_iris.feature_names

# step4) 시각화
# 1. graphviz 설치(window)
# down 주소 => https://graphviz.gitlab.io/_pages/Download/Download_windows.html
# 설치위치 (C:\Program Files\Graphviz)

# 2. graphviz 설치(python)
# pip install graphviz(cmd에서 수행)

# 3. python path 설정
import os
os.environ['PATH'] += os.pathsep + 'C:/Program Files/Graphviz/bin'

import graphviz

from sklearn.tree import export_graphviz
export_graphviz(m_dt,                           # 모델명 
                out_file="tree.dot", 
                class_names=load_iris().target_names,
                feature_names=load_iris().feature_names, 
                impurity=False, 
                filled=True)

with open("tree.dot", encoding='UTF8') as f:
    dot_graph = f.read()

g1 = graphviz.Source(dot_graph)
g1.render('dt_1', cleanup=True) 


# step5) 튜닝
# min_samples_split : 최소 가지치기 기준 
# max_depth : 나무의 복잡도 제어
# max_features : 각 노드의 기준 선택 시 고려되는 설명변수 후보의 수

vscore_tr = [] ; vscore_te = []

for i in range(2, 11) : 
    m_dt = dt(min_samples_split = i)
    m_dt.fit(train_x, train_y)  
    vscore_tr.append(m_dt.score(train_x, train_y))
    vscore_te.append(m_dt.score(test_x, test_y))

import matplotlib.pyplot as plt
plt.plot(range(2,11), vscore_tr, label='train')
plt.plot(range(2,11), vscore_te, label='test')
plt.legend()

# 랜덤포레스트
from sklearn.ensemble import RandomForestClassifier as rf
m_rf = rf()
m_rf.fit(train_x, train_y)
m_rf.score(test_x, test_y)  # 97.37%

m_rf.feature_importances_

# 튜닝
# n_estimators : tree의 수(100개 기본)
# max_features : 각 노드 기준 선택 시 고려되는 설명변수의 후보의 수
vscore_tr = [] ; vscore_te = []

for i in range(2,101) :
    m_rf = rf(n_estimators = i)
    m_rf.fit(train_x, train_y)
    vscore_tr.append(m_rf.score(train_x, train_y))
    vscore_te.append(m_rf.score(test_x, test_y)) 

# 매개변수 튜닝 결과 시각화
plt.plot(range(2,101), vscore_tr, label='train')
plt.plot(range(2,101), vscore_te, label='test')
plt.legend()


# GradientBoosting Tree
from sklearn.ensemble import GradientBoostingClassifier as gb

m_gb = gb()
m_gb.fit(train_x, train_y)
m_gb.score(test_x, test_y)  # 97.37%


