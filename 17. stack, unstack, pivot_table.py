# -*- coding: utf-8 -*-

# 자료 구조 형태
# long data(tidy data)
# - 각 속성을 컬럼으로 표현

# 지점
# A
# B
# C

# wide data(cross table : 교차표)
# - 하나의 속성을 갖는 데이터가 각 종류마다 서로 다른 컬럼으로 분리(나열)

#          A    B    C
# 판매량

# stack과 unstack
# 1. stack 
# wide -> long

# 2. unstack
# long -> wide

run my_profile
kimchi = pd.read_csv('kimchi_test.csv', encoding='cp949')

# kimchi 데이터를 연도별 제품별 수량의 총 합
df1 = kimchi.groupby(['판매년도', '제품'])['수량'].sum()

df1.unstack()                 # 인덱스의 가장 하위 레벨이 unstack 처리
df2 = df1.unstack(level=0)    # 인덱스의 특정 레벨을 unstack 처리 가능

df2.stack()                   # 컬럼이 인덱스의 하위 레벨로 stack 처리

# pivot_table
# 교차표 작성


# 예제 - kimchi data를 사용하여 아래처럼 표현
# 판매처   대형마트  백화점   편의점
# 판매월
# 1         1000    1001
# 2
# 3
# 4

kimchi.pivot_table(index='판매월',     # index 방향에 배치할 컬럼명
                   columns='판매처',   # column 방향에 배치할 컬럼명
                   values = '수량',    # 교차표에 작성할 값을 갖는 컬럼명 
                   aggfunc = 'sum')   # 그룹함수

# 예제 - kimchi data를 사용하여 연도별, 제품별 판매금액의 총 합을 교차표로 작성
kimchi.pivot_table(index='판매년도', columns='제품', values='판매금액', aggfunc = 'sum')

# 멀티 인덱스
# 인덱스나 컬럼이 여러 레벨로 표현
# 상위 레벨을 0, 하위 레벨로 갈수록 숫자 증가


# [ 연습 문제 ]
# student.csv 파일을 읽고
# 학년별,성별(index 방향), 학과별 키평균의 교차표 생성
std = pd.read_csv('student.csv', encoding='cp949')
pd.set_option('display.max_columns', 20)             # 출력되는 컬럼수 조절

# 성별 가공)
std.dtypes
std['성별'] = std['JUMIN'].astype('str').str[6].replace({'1':'남자','2':'여자'})

# 교차표 생성)
std.pivot_table(index=['GRADE','성별'], columns = 'DEPTNO1', values= 'HEIGHT', dropna=False)

