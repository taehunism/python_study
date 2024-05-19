#패턴, 메타캐릭터를 사용해서 함수를 사용해 응용
#자주 쓰이는 함수들
#-grouping()
#-match()
#-findall()
#-sub()

#정규 표현식 활용 실습
import re
#grouping
m = re.search(r'(\w+)@(.+)', 'ktaeh524@gmail.com') # 한 글자 이상의 문자 @ 한 글자 이상의 문자
print(m)
print(m.group(1))
print(m.group(2))
print(m.group(0))

#찾아주는 녀석 search
m = re.match(r'\d\d\d', 'my number is 123') #match는 앞에서부터 틀리면 None
print(m)
#완전 딱 맞아야되는 match
m = re.match(r'\d\d\d', '123 is my number') #match는 앞에서부터 틀리면 None
print(m)

#모두 찾아 리스트로 반환
m = re.findall(r'[\w]+@[\w.]+', 'abc ktaeh524@gmail.com fortaehun@gmail.con taehunism@inu.ac.kr')
print(m)

#sub 찾은 변수 치환
m = re.sub(r'[\w]+@[\w.]+', 'E-Mail', 'abc ktaeh524@gmail.com fortaehun@gmail.con taehunism@inu.ac.kr')
print(m)

email_re = re.compile(r'[\w]+@[\w.]+') #정규식 미리 제작 compile() 함수 사용
m = email_re.findall('abc ktaeh524@gmail.com fortaehun@gmail.con taehunism@inu.ac.kr')
print(m)

text = '''
홍길동, 010-111-2222
김길동, 010-3333-4444
최길동, 010-5555-6666
'''
number_re = re.compile(r'(\d{3}-\d{3,4})-(\d{4})')
m = number_re.findall(text)
print(m)
m = number_re.sub('\g<1>-####', text) #그룹 1번에 매칭되는 패턴을 치환해서 리턴
print(m)
