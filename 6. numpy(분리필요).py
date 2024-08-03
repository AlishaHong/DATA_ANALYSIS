# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 18:25:44 2021

@author: Hong
"""

# 자료 구조
# 1. 리스트
# 2. 튜플
# 3. 딕셔너리
# 4. 세트
# 5. 배열(numpy)
# 6. Series(pandas)
# 7. DataFrame(pandas)

# numpy
# 배열(array) 생성, 연산, ...

# array(배열)
# 하나의 데이터 타입 허용
# 다차원 자료 구조

import numpy as np

# 1. 생성
np.array([1,2,3])                                  # 1차원 array
np.array([[1,2,3],[4,5,6],[7,8,9]])                # 2차원 array
np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) # 3차원 array

a1 = np.arange(1,26).reshape(5,5)
type(a1)

# 2. 색인 : array[행선택, 열선택]
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
a2[1,:]     # 두 번째 행 선택(차원 축소 발생)
a2[:,1]     # 정수색인, 두 번째 행 선택(차원 축소 발생)
a2[:,1:2]   # 슬라이스색인, 두 번째 행 선택(차원 축소 발생 X)

a2[[0,2],:] # 1,3 행 선택
a2[:,[0,2]] # 1,3 컬럼 선택

a2[1,1]           # 5 리턴 
a2[[1,2],[1,2]]   # [5,9] 리턴 => a2[1,1], a2[2,2] 두 개의 포인트(점)가 출력이 된다
a2[np.ix_([1,2],[1,2])]   # [5,9] 리턴 => a2[1,1], a2[2,2] 두 개의 포인트(점)가 출력이 된다

a2[a2 > 5]          # 전체 데이터에서 5보다 큰 데이터만 추출
a2[a2[:,0] >= 5, :] # 첫번째 컬럼이 5이상인 행 선택(조건의 결과를 행 방향에 색인값으로 전달!!!)

# 3. 메서드
dir(a2)      # array 객체에 전달 가능한 메서드 목록

a2.dtype     # numpy 구성 자료 타입
a2.shape     # numpy 모양
a2.shape[0]  # numpy 행의 수
a2.shape[1]  # numpy 컬럼 수

a2.reshape(1,9)  # array 모양 변경
a2.ndim          # array 차원

# 4. 연산
[1,2,3] + [4,5,6]  # 리스트는 서로 연산 불가(확장으로 해석)
np.array([1,2,3]) + np.array([4,5,6])  # 서로 사이즈가 같은 배열끼리 연산 가능

# 5. 형 변환 메서드
a2.astype('float')  # 실수로 변경
a2.astype('int')    # 정수로 변경
a2.astype('str')    # 문자로 변경

# 6. np.where 함수
# if문의 축약형
# np.where(조건, 참리턴, 거짓리턴)

np.where(a2 > 5, 'A', 'B')   # 5보다 크면 'A', 작거나 같으면 'B'

if a2 > 5 :    # 여러 대상의 조건 결과를 if문에 전달할 수 없음(반복문 필요)
    'A'
else :
    'B'

# 7. 산술 연산 메서드
a2.sum()    # 전체 총 합
a2.mean()   # 전체 평균
a2.var()    # 전체 분산
a2.std()    # 전체 표준편차
a2.min()    # 전체 최솟값
a2.max()    # 전체 최댓값

(a2 > 5).sum()   # a2에서 5보다 큰 값의 수
(a2 > 5).any()   # a2에서 5보다 큰 값이 하나라도 있을 경우 참
(a2 > 5).all()   # a2에서 모두 5보다 클 경우 참

a2.sum(axis=0)   # 행별 총 합(서로 다른 행끼리, 세로 방향 연산)
a2.sum(axis=1)   # 컬럼별 총 합(서로 다른 컬럼끼리, 가로 방향 연산)

# [ 참고 : 축 번호]
# 2차원 : 행(0) , 열(1)
# 3차원 : 층(0), 행(1) , 열(2)


# 8. 전치 메서드
# 1) T : 행과 열 전치
a1 = np.arange(1,9).reshape(4,2)
a1.T

# 2) swapaxes : 두 축을 전달받아 두 축을 서로 전치, 전달 순서 중요 X
a1.swapaxes(0,1)    
a1.swapaxes(1,0)    

# 3) transpose : 원본의 차원에 맞는 축번호를 인수에 차례대로 전달하여 그대로 전치
#                전달되는 순서 중요!!
               
a1.transpose(0,1)  # 원본 그대로 출력
a1.transpose(1,0)  # 행과 열 전치


# 9. 외부 파일 입출력
# 1. 파일 불러오기
np.loadtxt(fname,         # 파일명
           dyte,          # 데이터타입(기본값 float)
           delimiter,     # 필드 구분기호
           skiprows,      # 스킵할 행의 수
           usecols,       # 선택할 컬럼 값(위치)
           encoding)      # 인코딩 옵션

np.loadtxt('file1.txt', delimiter=',', dtype = 'int')

# 2. 파일 내려쓰기
np.savetxt(fname,         # 파일명
           X,             # 객체명
           fmt,           # 출력형식
           delimiter,     # 출력시 분리 구분 기호
           header,        # 헤더 출력 여부(file의 첫 문자열)
           encoding)      # 인코딩 옵션

np.savetxt('text1.txt', a2, delimiter=',', fmt = '%s')

[ 참고 : fmt 전달/변경 방식 ]
%s : 문자열
%f : 실수
%d : 정수

'%s' % 123     # '123'
'%f' % 123     # '123.000000'
'%.2f' % 123   # '123.00'

'%7d' % 123    # '    123'

