# -*- coding: utf-8 -*-
# cancer_test.csv 파일을 읽고
run my_profile
df1 = pd.read_csv('cancer_test.csv')
df1.columns
df1.dtypes

# 1. radius_mean, texture_mean, texture_se, smoothness_se이 NA인 행을 제거 한 후 총 행의 수 리턴
df1['radius_mean'].isnull().sum()      # NA 개수
df1['texture_mean'].isnull().sum()     # NA 개수
df1['texture_se'].isnull().sum()       # NA 개수
df1['smoothness_se'].isnull().sum()    # NA 개수

vbool = df1['radius_mean'].isnull() & df1['texture_mean'].isnull() & df1['texture_se'].isnull() &  df1['smoothness_se'].isnull()
vbool.sum()         # 컬럼 4개가 모두 NA인 행의 수

df1.loc[vbool, :]   # 컬럼 4개가 모두 NA인 행 확인

df1.shape[0] - vbool.sum()   # 565건

print(df1.shape[0] - vbool.sum())


# -- 
nrow = df1.dropna(subset=['radius_mean', 'texture_mean', 'texture_se', 'smoothness_se'], how='all').shape[0]
print(nrow)

# 2. concavity_mean의 standard scaling 후 결과가 0.1 이상인 값의 개수 출력
# standard scaling(변수 표준화) = (원데이터 - 평균) / 표준편차
# minmax scaling = (원데이터 - 최소) / (최대 - 최소)

vscale = (df1['concavity_mean'] - df1['concavity_mean'].mean()) / df1['concavity_mean'].std()
(vscale >= 0.1).sum()


# 3. texture_se의 상위 10% 값(NA를 제외한 건수의 10%)을 이상치로 가정하고 
# 10%를 제외한 값의 최대값으로 수정후 평균을 소수점 둘째자리로 반올림하여 출력

# 이상치 건 수 확인
df1['texture_se'].dropna().shape[0]                             # 565건 
nx = int(np.trunc(df1['texture_se'].dropna().shape[0] * 0.1))   # 56건

# 이상치를 제외한 나머지에 대한 평균
vrank = df1['texture_se'].rank(ascending=False, method='first')

df1.loc[vrank > nx, 'texture_se']                       # 정상치 데이터
vmax = df1.loc[vrank > nx, 'texture_se'].max()          # 정상치 데이터 평균

df1.loc[vrank <= nx, 'texture_se']                      # 이상치 데이터
df1['texture_se'].sort_values(ascending=False)[:nx]     # 이상치 데이터

df1.loc[vrank <= nx, 'texture_se'] = vmax               # 이상치 데이터 수정

print(round(df1['texture_se'].mean(), 2))


# 4. symmetry_mean의 결측치를 최소값으로 수정 후 평균을 소수점 둘째자리로 반올림하여 출력
df1['symmetry_mean'].min()     # 문자값이 삽입되어 있음을 확인

from numpy import nan as NA
df1['symmetry_mean'] = df1['symmetry_mean'].replace('-', NA)
df1['symmetry_mean'].astype('float')                           # '.'이 있어서 숫자로 변경 불가

df1['symmetry_mean'] = df1['symmetry_mean'].replace('.', NA)
df1['symmetry_mean'].astype('float')                           # 'pass'가 있어서 숫자로 변경 불가

df1['symmetry_mean'] = df1['symmetry_mean'].replace('pass', NA)
df1['symmetry_mean'] = df1['symmetry_mean'].astype('float')    # 'pass'가 있어서 숫자로 변경 불가

df1['symmetry_mean'].replace([',','.','-'], NA)                # 동시 치환 가능(참고)

# 최소값 확인
vmin = df1['symmetry_mean'].min()

# 결측치 수정
df1['symmetry_mean'] = df1['symmetry_mean'].fillna(vmin)

# 평균 확인
print(round(df1['symmetry_mean'].mean(),2))
