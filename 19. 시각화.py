# -*- coding: utf-8 -*-
run my_profile

# 시각화
import matplotlib.pyplot as plt

# 1. 선그래프 : plot
plt.plot([1,2,3,4],
         [10,20,30,40],
         marker='^',
         linestyle='--',
         color='red')

s1 = Series([10,20,30,40])
s1.plot()
s1.plot(xticks=[0,1,2,3],
        ylim=[0,100],
        xlabel='x name',
        ylabel='y name',
        rot=90,
        title='name',
        marker='^',
        linestyle='--',
        color='red')

plt.xticks(ticks=,      # 눈금 좌표
           labels=,     # 눈금 이름
           rotation=)   # 회전 각도

plt.xticks(ticks=[0,1,2,3], labels=['a','b','c','d'], rotation=180)
plt.ylim([0,100])
plt.ylabel('y name',
           rotation=0, 
           loc='top',        # 위치 
           labelpad=30,      # 축이름과 축눈금과의 간격
           fontdict=font1)        # 글씨체와 관련된 옵션(딕셔너리)

# fontdict
font1 = {'family' : 'Malgun Gothic',
         'weight' : 'bold', 
         'size' : 15,
         'color' : 'red',
         'style' : 'italic'}

plt.title('그래프 제목', fontdict=font1)

plt.rc('font', family='Malgun Gothic')      # global 옵션 변경
plt.rcParams.keys()                         # global 옵션 변경 방법(종류) 확인 가능

# 데이터프레임의 선 그래프 출력
df1 = DataFrame({'apple':[10,20,30,40], 'banana':[49,39,30,12], 'mango':[10,32,43,40]})
df1.index = ['a','b','c','d']
df1.index.name = '지점'
df1.columns.name = '과일명'

df1.plot()                   # 컬럼별 서로 다른 선그래프 출력 가능

plt.legend(fontsize=9,
           loc='best',
           title='과일 이름')

# 2. barplot
df2 = pd.read_csv('kimchi_test.csv', encoding='cp949')
kimchi = df2.pivot_table(index='판매월', columns='제품', values='수량', aggfunc='sum')

kimchi.plot(kind='bar')
plt.title('김치별 판매수량 비교')
plt.ylim([0,300000])
plt.ylabel('판매수량')

# =============================================================================
# 3. pie chart
# =============================================================================
# 환경 설정
ratio = [34, 32, 16, 18]
labels = ['Apple', 'Banana', 'Melon', 'Grapes']
colors = ['#d96353', '#53d98b', '#53a1d9', '#fab7fa']   
colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0']
explode = [0.1, 0.1, 0.1, 0.1]
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(ratio,                  # 각 파이 숫자
        labels=labels,          # 각 파이 이름
        autopct='%.1f%%',       # 값의 표현 형태
        startangle=260,         # 시작위치
        radius = 0.8,           # 파이 크기
        counterclock=False,     # 시계방향 진행 여부
        explode = explode,      # 중심에서 벗어나는 정도 설정(각각 서로 다른 숫자 전달 가능)
        colors=colors,          # 컬러맵 전달 가능
        shadow=False,           # 그림자 설정
        wedgeprops=wedgeprops)  # 부채꼴 모양 설정

# =============================================================================
# 4. hist
# =============================================================================
s1 = Series(np.random.randn(1000))
s1.hist(bins=4)       # 막대의 개수 또는 계급의 구간 전달

plt.hist(s1, 
         bins,
         density = False)       # True 설정 시 막대 아래 총 면적이 1이 되는 밀도함수 출력(Y축 값이 확률로 변경)
plt.hist(s1, density = True)
s1.plot(kind='kde')             # 커널밀도함수 출력, 연속형 히스토그램

# =============================================================================
# 5. scatter
# =============================================================================
# iris data loading
from sklearn.datasets import load_iris
iris = load_iris()
iris.keys()                    # dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])

print(iris['DESCR'])
iris_x = iris['data']
xnames = iris['feature_names']

plt.subplot(2,2,1)
plt.scatter(iris_x[:,0],       # x축 좌표
            iris_x[:,1],       # y축 좌표
            c = iris_x[:,1])   # color(색 하나 전달 시 모두 동일한 색 출력, 
                               # 서로 다른 숫자 전달 시 서로 다른 색 표현(채도)

plt.spring()                # color map(gray, bone, pink, spring, summer, autumn, winter, cool, hot, copper,
                            #           viridis, plasma, infemo, magma, flag, prism, jet, nipy_spectral, hsv)
plt.xlabel(xnames[0])       
plt.ylabel(xnames[1])
plt.colorbar()              # 컬러바 출력 시

plt.subplot(2,2,2)
plt.scatter(iris_x[:,1], iris_x[:,2], c = iris_x[:,2])
plt.summer()                # color map
plt.xlabel(xnames[1])
plt.ylabel(xnames[2])
plt.colorbar()              # 컬러바 출력 시

plt.subplot(2,2,3)
plt.scatter(iris_x[:,2], iris_x[:,3], c = iris_x[:,3])
plt.autumn()                # color map
plt.xlabel(xnames[2])
plt.ylabel(xnames[3])
plt.colorbar()              # 컬러바 출력 시

plt.subplot(2,2,4)
plt.scatter(iris_x[:,3], iris_x[:,0], c = iris_x[:,0])
plt.winter()                # color map
plt.xlabel(xnames[3])
plt.ylabel(xnames[0])
plt.colorbar()              # 컬러바 출력 시

# =============================================================================
# 6. boxplot
# =============================================================================
plt.boxplot(iris_x)
plt.xticks(ticks=[1,2,3,4], labels=xnames)
