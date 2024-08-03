# -*- coding: utf-8 -*-

# 논리 연산자
and
or
not

v1 = 1
(v1 >= 3) and (v1 <= 7)   # 3과 7사이
(v1 >= 3) & (v1 <= 7)     # 3과 7사이

(v1 <= 3) or (v1 >= 7)   # 3보다 작거나 같고 또는 7보다 크거나 같은지 
(v1 <= 3) | (v1 >= 7)   # 3보다 작거나 같고 또는 7보다 크거나 같은지 

not(v1 == 1)

# 조건문 : 조건에 따른 연산처리 진행 시 필요
# if문

# [ 형식 ]
if 조건 :
    참일때 실행 문장
else :
    거짓일때 실행 문장
    
    
if 조건1 :
    조건1이 참일때 실행 문장
elif 조건2 :
    조건1이 거짓이면서 조건2가 참일때 실행 문장
else :
    조건1,2 모두 거짓일때 실행 문장
    

v1 = 10    
if v1 > 5 :
    print('A')
else :
    print('B')


l1 = [1,3,5,15,25]
if l1 > 5 :             # 불가
    print('A')
else :
    print('B')
    

# 반복문
# 객체의 각 원소에 동일한 연산처리를 진행 할 경우 사용
# 1. for문 : 정해진 횟수, 대상이 있을 경우
# [ 문법 ]

for 반복변수 in 반복대상(범위) :
    반복할 실행 문장
    
# 1 ~ 10까지 출력
for i in range(1,11) :
    print(i)

# 예제
# 다음의 리스트를 선언하고 5보다 큰 경우 'A', 5보다 작거나 같은 경우 'B'
l1 = [1,3,5,15,25] 

for i in l1 :
    if i > 5 :
        print('A')
    else :
        print('B')

# 예제
# 위 리스트에 각 원소에 10을 더해서 출력
l1 + 10        # 불가

for i in l1 :
    print(i + 10)

l2 = for i in l1 :   # for문의 결과를 바로 변수에 저장 불가
    i + 10

# 정답    
l2 = []
for i in l1 :   # for문의 결과를 바로 변수에 저장 불가
   l2.append(i + 10)
l2    
    

# 2. while문 : 조건에 따른 반복을 실행할 경우

# [ 문법 ]
while 조건 :
    조건이 참 일때 반복 문장
    
# 예제
# while문으로 1~10까지 출력
i = 1
while i <= 10 :
    print(i)
    i = i + 1
    

# 문제
# 1~100까지의 총 합

vsum = 0
for i in range(1,101) :
    vsum = vsum + i
vsum

i    vsum        일반화
1     1          vsum + 1
2     1+2        vsum + 2
3     1+2+3      vsum + 3
4     1+2+3+4    vsum + 4   => vsum + i

# 문제
# 1~100까지의 짝수 총 합

vsum = 0
for i in range(1,101) :
    if i % 2 == 0 :
        vsum = vsum + i
vsum


# 반복 제어문
# 1. continue : 특정 조건일 경우 반복문 스킵
# 2. break : 특정 조건일 경우 반복문 종료
# 3. exit : 특정 조건일 경우 프로그램 종료
# 4. pass : 문법적으로 오류를 발생시키지 않기 위한 자리를 채우는 역활

# 예제 : 1~10출력, 5제외    
for i in range(1,11) :
    if i == 5 :
        continue
    print(i)    

# 예제 : 1~10출력, 5를 만나면 반복문 종료    
for i in range(1,11) :
    if i == 5 :
        break
    print(i)    
    
# 예제 : 1~10출력, 5를 만나면 반복문 종료    
for i in range(1,11) :
    if i == 5 :
        exit(0)
    print(i)    

# pass 사용 예제
v1 = 1    
if v1 > 10 :
    pass            # 이 자리를 비워두면 에러 발생하므로 pass 삽입
else :
    print('b')


# [ 문제 ]
# 1부터 100까지의 누적합이 최초 2000이상이 되는 시점의 k값과 총 합을 출력
# 1 + 2 + .... + k >= 2000 

vsum = 0
for i in range(1,101) :
    vsum = vsum + i
    if vsum >= 2000 :
        break

print(i, vsum)    










