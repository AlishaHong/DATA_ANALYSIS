# -*- coding: utf-8 -*-
# =============================================================================
# Sales 예측 모델링(회귀)
# sales_train_x,  sales_train_y파일을 가지고 최적의 회귀 모형을 만든 뒤
# sales_test_x.csv 파일의 데이터에 대한 Sales 예측값을 제출
# =============================================================================
import pandas as pd
X_train = pd.read_csv('sales_train_x.csv')
y_train = pd.read_csv('sales_train_y.csv')
X_test = pd.read_csv('sales_test_x.csv')
y_train = y_train['Item_Outlet_Sales']             # Y를 시리즈 형태로 만들어야 함

# =============================================================================
# 1. 각 컬럼 데이터 타입 확인
# =============================================================================
X_train.dtypes

# Item_Weight                  float64
# Item_Visibility              float64
# Item_Type                     object     # 문자컬럼 => 숫자변경
# Item_MRP                     float64
# Outlet_Establishment_Year      int64
# Outlet_Size                   object     # 문자컬럼
# Outlet_Type                   object     # 문자컬럼
# dtype: object

# =============================================================================
# 2. 결측치 확인
# =============================================================================
X_train.isnull().sum()

# Item_Weight                  1463         # 결측치 대치 필요
# Item_Visibility                 0
# Item_Type                       0
# Item_MRP                        0
# Outlet_Establishment_Year       0
# Outlet_Size                  2410         # 결측치 대치 필요
# Outlet_Type                     0
# dtype: int64

# =============================================================================
# 3. 데이터 신뢰성 확인
# =============================================================================
# - 결측치 처리가 필요한 데이터가 있는지(. , -, ?, !)
# - 수치형 데이터에 의미없는 수치가 삽입되었는지
(X_train['Item_Visibility'] == 0).sum()
(X_train['Item_Visibility'] < 0).sum()


# =============================================================================
# 4. Item_Weight 결측치 처리
# =============================================================================
# Item_Weight 같으면 Item_Weight이 비슷할것으로 예상
# Item_Type 별 Item_Weight의 평균을 구해 나머지를 대치

weight_mean = X_train.groupby('Item_Type')['Item_Weight'].mean()

fill_weight_value_train = X_train['Item_Type'].map(weight_mean)
X_train['Item_Weight'] = X_train['Item_Weight'].fillna(fill_weight_value_train)

fill_weight_value_test = X_test['Item_Type'].map(weight_mean)
X_test['Item_Weight'] = X_test['Item_Weight'].fillna(fill_weight_value_test)

# Item_Weight   Item_Type            Item_Type     mean
# 12              Canned              Canned       12.5
# NA              Canned


# =============================================================================
# 5. Outlet_Size 결측치 대치
# =============================================================================
from pandas import Series
size_dict = Series(['Small', 'Medium', 'Medium', 'Small'], 
                   index = ['Supermarket Type1', 'Supermarket Type2', 
                            'Supermarket Type3', 'Grocery Store'])

fill_size_value_train = X_train['Outlet_Type'].map(size_dict)
X_train['Outlet_Size'] = X_train['Outlet_Size'].fillna(fill_size_value_train)

fill_size_value_test = X_test['Outlet_Type'].map(size_dict)
X_test['Outlet_Size'] = X_test['Outlet_Size'].fillna(fill_size_value_test)


X_train


# =============================================================================
# 6. 라벨 인코딩*** : 설명변수에 문자값이 있을 경우 모델링 불가 
#    => 숫자로 변경(각 문자들을 구분하기 위한 의도)
# 단순하게 0,1,2,3 등의 서로 다른 숫자로 변경할수도 있지만
# 순서가 정해져 있는 범주형일 경우 사용자가 직접 숫자의 크기를 조절하기도 함
# =============================================================================
# Item_Type 변경 : abc 순서대로 숫자 부여

from sklearn.preprocessing import LabelEncoder
m_le = LabelEncoder()
X_train['Item_Type'] = m_le.fit_transform(X_train['Item_Type'])
X_test['Item_Type'] = m_le.transform(X_test['Item_Type'])

# Outlet_Size 변경 : 사용자가 직접 번호 부여****
dict1 = {'Small':1, 'Medium':2, 'High':3}
X_train['Outlet_Size'] = X_train['Outlet_Size'].map(dict1)
X_test['Outlet_Size'] = X_test['Outlet_Size'].map(dict1)

# Outlet_Type 변경 : 빈도수를 변경할 숫자값으로 사용(크기의 차이를 반영 목적)
dict2 = X_train['Outlet_Type'].value_counts()
X_train['Outlet_Type'] = X_train['Outlet_Type'].map(dict2)
X_test['Outlet_Type'] = X_test['Outlet_Type'].map(dict2)

# =============================================================================
# 7. 모델링
# =============================================================================
# train, test 분리
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(X_train, y_train, random_state=0)

# modeling
from sklearn.ensemble import RandomForestRegressor
m_rf_reg = RandomForestRegressor()
m_rf_reg.fit(train_x, train_y)
m_rf_reg.score(train_x, train_y)   # 0.93804
m_rf_reg.score(test_x, test_y)     # 0.55920

test_y_hat = m_rf_reg.predict(test_x)


# =============================================================================
# 8. 평가(RMSE)
# =============================================================================
from sklearn.metrics import mean_squared_error
mean_squared_error(test_y, test_y_hat)                    # MSE
mean_squared_error(test_y, test_y_hat, squared=False)     # RMSE

# =============================================================================
# 9. 제출
# =============================================================================
from pandas import DataFrame

test_predict = m_rf_reg.predict(X_test)
df_result = DataFrame({'ID':X_test.index, 'Y':test_predict})

df_result.to_csv('test_t1.csv', index=False)

# < 제출형식 >
# ID   Y
# 0    ...
# 1
# 2
# 3







