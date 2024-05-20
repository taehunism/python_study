#정규표현식 Regular Expression
#특정한 패턴과 일치하는 문자열을 찾기 위해 사용
#문자열 검색, 치환, 제거 용도로 사용
#대부분의 시스템이나 프로그래밍 언어에서 표준으로 사용

#a,A,1 등 문자 하나는 정확히 하나의 문자와 일치
#.(마침표) : 한개의 문자와 일치 #아무 문자
#\w : 문자 (a~z , A~Z, 0~9)
#\d : 숫자
#\s : 공백문자
#이스케이프 문자 : \t(tab), \n(newline)

#raw string 
a = "abc\ndef"
# \n은 이스케이프n은 줄바꿈 문자이다.
print(a)
b = r'abe\ndef' #r을 사용하여 정규표현
print(b)

import re #regular expression
m = re.search('adc', '123abc') #파라미터 : 정규식패턴, 검색대상 
# 찾으면 match 객체 리턴 찾지 못하면 None 리턴
print(m)

m = re.search(r'\d\d\d', 'def123abc') #숫자 3개 연속되는 거 찾기
print(m)

m = re.search(r'..\w\w\w', '123!@abc')
print(m)

m = re.search(r'[cem]at', 'bat') #[cem]은 문자의 범위 지정 
#.은 무엇이든 잡아냄 
print(m)

m = re.search(r'0[0-3]','031')
print(m)

m = re.search(r'b\w?a', 'baa') # b\w+a는 b로 시작되고 어떤 문자가 한 번 이상 반복 맨 마지막은 a로 끝나야함
print(m)

m = re.search(r'https?', 'http://www.naver.com') #문자 뒤에 ?가 붙어있다면 그 문자는 있어도 없어도 상관없음 don't care
print(m)