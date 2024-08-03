# -*- coding: utf-8 -*-

# 문자열 : 여러 문자의 배열
'a'
'ab'
'abc is ....'

# 함수와 메서드의 차이
# 함수 : 함수(대상)
# 메서드 : 대상.메서드

# 1. 대소치환
v1 = 'abcde'
v1.upper()            # 대문자 치환
'ABCD'.lower()        # 소문자 치환
'abc def'.title()     # camel 표기법(단어의 첫 글자만 대문자 표시)

# 2. 색인(문자열 추출)
'abcd'[0]
'abcd'[0:3]

# ex) '031)345-0834' 에서 지역번호 추출
vtel = '031)345-0834'
vtel[0:3]

# 3. 문자열의 시작, 끝 여부 확인
v1.startswith(prefix,    # 시작값 확인 문자
              start,     # 확인할 시작 위치
              end)       # 확인할 끝 위치

v1.startswith(prfeix='a')
v1.startswith('b')
v1.startswith('b', 1)        # v1[1:].startswith('b')와 같다

v1.endswith(suffix,
            start,
            end)

v1.endswith('e')
v1.endswith('E')


# 4. 앞 뒤 공백 또는 문자 제거
' abc' == 'abc'
' abc'.strip()      # 양쪽 공백 제거
'abc'.strip('a')    # 양쪽 문자 제거
'abaca'.strip('a')  # 양쪽 문자 제거(중간 글자 삭제 불가)

' abcd '.lstrip()   # 왼쪽에서 공백 또는 글자 제거
' abcd '.rstrip()   # 오른쪽에서 공백 또는 글자 제거

# 5. 치환
'abcaba'.replace(old,  # 찾을 문자열
                 new)  # 바꿀 문자열

'abcaba'.replace('a','A')     # 치환
'abcaba'.replace('ab','AB')   # 치환
'abcaba'.replace('ab','')     # 'ab' 단어 모두 삭제


# 6. 문자열 분리
v1.split(sep)    # 분리구분기호
'a/b/c/d'.split('/')[1]

# 7. 위치값 리턴
'abcd'.find(sub,     # 위치값을 찾을 대상
            start,   # 찾을 위치(시작점)
            end)     # 찾을 위치(끝점)

v1.find('b')

# ex. 전화번호에서 지역번호 추출 시 ')'위치를 확인하여 그 이전까지 추출
vnum = vtel.find(')')
vtel[0:vnum]

# 8. 포함 횟수
'abcabc'.count('a')   # 'a'가 포함된 횟수

# 9. 형 확인 함수
v1.isalpha()    # 문자 확인
v1.isnumeric()  # 숫자 확인
v1.isupper()    # 대문자 확인
v1.islower()    # 소문자 확인

# 10. 문자열 결합
'a' + 'b'

# 11. 문자열 길이
len(v1) 


# [ 연습 문제 ]
vname = 'smith'
vemail = 'abcd@itwill.com'
jumin = '901211-1223453'

# 1. 이름의 두 번째 글자가 m인지 여부 확인
vname[1] == 'm'

# 2. vemail에서 이메일 아이디만 추출
vemail[0:4]

vno1 = vemail.find('@')
vemail[0:vno1]

# 3. 주민번호에서 여자인지 확인
jumin[7] == '2'


























