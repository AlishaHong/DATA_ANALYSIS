# -*- coding: utf-8 -*-

# 사용자 정의 함수
# 사용자가 정의하는 함수의 형태
# input과 output과의 관계를 내부에서 정의
# def, lambda(축약형)

# [ 함수의 정의 ]
# f(x) = x + 1
# f(a) = a + 1

# 1. def 방식
# [ 문법 ]
def 함수이름(인수1, 인수2, ...) :
    함수 본문
    return 리턴객체

# 예제 
# 숫자를 넣어서 곱하기 10 리턴
# f_pro(10) => 100

def f_pro(x) :
    v1 = x * 100
    return v1

f_pro(10)

# 예제
# 두 숫자를 넣어서 두 숫자의 곱 리턴
# f_pro2(1,10) => 10

def f_pro2(x, y) :
    return(x * y)

f_pro2(2,10)

# 인수에 디폴트값(기본값 선언)
def f_pro2(x=1, y) :      # 첫 번째 인수에 기본값을 정의하면 뒤에 나오는 인수도
    return(x * y)         # 기본값을 선언해야 함

def f_pro2(y, x=1) :      # 디폴트 값을 갖는 인수를 맨 뒤에 배치
    return(x * y)         

def f_pro2(x=1, y=1) :    # 모든 인수에 디폴트 값 선언
    return(x * y)        

    
# 2. lambda(축약형)
# 비교적 단순한 연산 및 리턴시 사용

# [ 문법 ]
# 함수명 = lambda 인수1, 인수2, ... : return값

# 예제 : 숫자를 넣어 10을 곱한 값 리턴
f1 = lambda x : x * 10
f1(5)

# [ 문제 ]
# 세 개의 숫자를 전달 받아 첫번째와 두번째의 합에 세번째 숫자의 곱 리턴

f2 = lambda x, y, z : (x + y) * z
f2(2,5,3)

# lambda에 기본값 전달
f2 = lambda x=0, y=0, z=1 : (x + y) * z


# map 함수
f1 = lambda x : x * 10
f1(4)

# 예제
# 아래 리스트에 각 원소에 10을 곱하는 값 리턴
l1 = [1,2,5,10]
f1(l1)            # l1 * 10이 되면서 리스트가 10번 반복

# 1) for문 처리
l2 = []
for i in l1 :
    l2.append(i * 10)
l2

# 2) 사용자 정의 함수 + map
map(func,      # 적용함수
    iterable)  # 추가인수

list(map(f1, l1))    # f1(1), f1(2), f1(5), f1(10)


# [ 문제 ]
# 숫자를 전달 받아 10보다 크면 3을 곱하고 작거나 같으면 2를 곱해 리턴
# 다음의 리스트에도 적용
l2 = [3,5,7,10]

def f3(x) :
    if x > 10 :
        v1 = x * 3
    else :
        v1 = x * 2
    return v1

f3(11)
f3(l2)  # error!

list(map(f3, l2))


# [ 문제 ]
# 부서번호와 급여를 전달받아
# 10번 부서는 급여의 10% + 100
# 20번 부서는 급여의 11% + 90
# 30번 부서는 급여의 12% + 90의 보너스를 리턴하고 다음의 값을 갖는 리스트에 적용
deptno = [10,10,20,30]
sal = [350, 330, 400, 420]

def f_bonus(deptno, sal) :
    if deptno == 10 :
        bonus = sal * 1.1 + 100
    elif deptno == 20 :
        bonus = sal * 1.11 + 90
    else :
        bonus = sal * 1.12 + 90
    return(round(bonus))

list(map(f_bonus, deptno, sal))

# map 함수의 장점 : 여러 객체(1차원)에 대한 동시 fetch가 가능
