# -*- coding: utf-8 -*-

# 나이브 베이즈 모델
# 베이즈 이론에 따라 사전, 사후 확률로 타겟을 예측하는 방법
# 문서 분류 등 텍스트 마이닝을 통한 텍스트 분류에 많이 사용

# 1. data loading
from sklearn.datasets import load_iris
iris = load_iris()
iris_x = iris.data
iris_y = iris.target

# 2. data split
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y, random_state=0)

# 3. modeling
from sklearn.naive_bayes import BernoulliNB     # 이진 데이터일 경우 적용
from sklearn.naive_bayes import GaussianNB      # 연속형 데이터일 경우
from sklearn.naive_bayes import MultinomialNB   # 카운트 데이터일 경우

m1 = GaussianNB()
m1.fit(train_x, train_y)
m1.score(test_x, test_y)   # 1.0

# 4. predict
vpre = m1.predict(test_x[0:1,:])   # 예측값 확인(번호)
iris.target_names[vpre][0]         # 예측값 확인(이름)

import numpy as np
np.round(m1.predict_proba(test_x[0:1,:]), 3)



# 로지스틱 회귀
# 회귀모델처럼 로그오즈를 설명변수의 선형 결합으로 해석
# 회귀식 추정을 통한 Y의 클래스의 분류를 수행
# 이상치 민감, 변수 스케일링, 변수 선택, 변수간 상관관계 등 고려

# 1. data loading
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
cancer_x = cancer.data
cancer_y = cancer.target

# 2. data split
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(cancer_x, cancer_y, random_state=0)

# 3. modeling
from sklearn.linear_model import LogisticRegression

m1 = LogisticRegression()
m1.fit(train_x, train_y)
m1.score(test_x, test_y)    # 95.10

m1.coef_       # 회귀 계수
m1.intercept_  # 회귀 절편

# 4. predict
vpre = m1.predict(test_x[0:1,:])   # 0
cancer.target_names[vpre]          # malignant

logy = m1.decision_function(test_x[0:1,:])  # log(P/1-P)

import numpy as np
np.exp(logy) / (1 + np.exp(logy))             # P(Y=1)
m1.predict_proba(test_x[0:1,:])               # 각 클래스별 예측 확률 출력
m1.predict_proba(test_x[0:1,:])[:,1]          # P(Y=1) 


# 전체 데이터셋에 대한 P(Y=1)일 확률 시각화
m1.decision_function(cancer_x)        # log odds
p1 = m1.predict_proba(cancer_x)[:,1]  # P(Y=1)

import matplotlib.pyplot as plt
p1.sort()
plt.plot(p1)
