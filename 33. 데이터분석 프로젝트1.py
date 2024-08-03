# -*- coding: utf-8 -*-

# 데이터 셋 : 암 종양의 양성/악성 여부 예측
# 1. data loading
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

cancer_x = cancer['data']
cancer_y = cancer['target']

cancer.target_names         # 'malignant'(y=0), 'benign'(y=1)

# 2. data split
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(cancer_x, cancer_y, random_state=0)

# 3. 데이터 전/후처리
# 변수선택 : 분석 결과에 안좋은 영향을 미치는 변수 제거, 영향력이 높은 변수 선택
# 변수변환 : 분석 결과에 더 좋은 영향을 미치는 변수의 형태로 변환, 결합
# ex) 게임당 킬수 : kill수 / 게임수
# 이상치/결측치 처리 
# 차원 축소 : 의미있는 인공변수 유도
# 변수 스케일링(표준화)

# 변수 스케일링
from sklearn.preprocessing import StandardScaler as standard
m_sc = standard()
m_sc.fit(train_x)
train_x_sc = m_sc.transform(train_x)
test_x_sc = m_sc.transform(test_x)

# 4. modeling(random forest, svm, knn, logistic regressor..., ann, ...)
from sklearn.svm import SVC
m_svm = SVC(probability=True)
m_svm.fit(train_x_sc, train_y)
m_svm.score(test_x_sc, test_y)    # 96.50

# 모델 간 비교, 모델 튜닝

# 5. prob 출력
prob = m_svm.predict_proba(test_x_sc)

prob_0 = prob[:,0]   # malignant(악성)의 확률
prob_1 = prob[:,1]   # benign(양성)의 확률

# 6. roc curve
from sklearn.metrics import roc_curve

fper, tper, thresholds = roc_curve(test_y, prob_1)

import matplotlib.pyplot as plt

plt.plot(fper, tper, marker = '.', color = 'red', label = 'ROC')
plt.plot([0,1],[0,1], color = 'green', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Roc Curve')
plt.legend()

# 7. auc
from sklearn.metrics import roc_auc_score
roc_auc_score(test_y, prob_1)    # 99.81
