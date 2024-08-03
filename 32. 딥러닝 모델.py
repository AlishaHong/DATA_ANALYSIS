# -*- coding: utf-8 -*-

# 0. 필요 모듈 설치 및 로딩
import tensorflow as tf
import keras

# 1. data loading
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
cancer_x = cancer['data']
cancer_y = cancer['target']

cancer_x.shape           # 569 행, 30개 설명변수
cancer.feature_names     # 설명변수 이름
cancer.target_names      # 'malignant' : 0, 'benign' : 1

# [ 참고 : 문자 데이터를 숫자 데이터로 변환하는 방법 ]
from pandas import Series, DataFrame
s1 = Series(['a','a','b','c'])

from sklearn.preprocessing import LabelEncoder
m_label = LabelEncoder()
m_label.fit_transform(s1)    # array([0, 0, 1, 2])


# 2. data split
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(cancer_x, cancer_y, random_state=0)

# 3. scaling
from sklearn.preprocessing import StandardScaler as standard
m_sc = standard()

m_sc.fit(train_x)
train_x_sc = m_sc.transform(train_x)
test_x_sc = m_sc.transform(test_x)

# 4. modeling(ann)
from keras.models import Sequential
from keras.layers.core import Dense

nx = train_x_sc.shape[1]         # 설명변수의 개수(30개)

model = Sequential()
model.add(Dense(15,                         # 두 번째 층의 노드의 수
                input_dim = nx,             # 설명변수 개수
                activation = 'relu'))       # 활성화 함수
model.add(Dense(2,                          # 출력층일 경우 종속변수의 개수
                activation = 'softmax'))

# 5. training
# step1) Y의 형태 바꾸기(Y_0, Y_1로 분할!!)
from keras.utils import np_utils
train_y = np_utils.to_categorical(train_y)
test_y = np_utils.to_categorical(test_y)

# Y   Y_0   Y_1
# 0    1     0
# 1    0     1

# Y   Y_A  Y_B  Y_C
# A    1    0    0
# B    0    1    0
# C    0    0    1

# step2) compile
model.compile(optimizer = 'adam',
              loss = 'categorical_crossentropy',
              metrics = ['accuracy'])

# step3) fit
model.fit(train_x_sc, train_y, epochs = 25)

# step4) evaluate
model.evaluate(test_x_sc, test_y)[1]   # 94.40

# 6. 자동 학습 중단(EarlyStopping)
from keras.callbacks import EarlyStopping
earlystopping = EarlyStopping(monitor = 'val_loss',              # 회귀모델 : mean_squared_error
                              patience = 10,                     # 분류모델 : val_loss
                              mode = 'auto')

model.fit(train_x_sc, train_y, epochs = 1000,
          validation_split = 0.25, callbacks = [earlystopping])

model.evaluate(test_x_sc, test_y)[1]
