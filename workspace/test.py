#숫자 포맷팅
a = '제 나이는 %d세 입니다. 다 다 다' % 34
print(a)

b = '제 이름은 %s 입니다.' % ('홍길동')
print(b)

c = '제 이름은 %s이고, 나이는 %d 입니다.' % ('홍길동', 30)
print(c)

d = '원주율은 %3.2f 입니다.' % 3.14213
print(d)
#문자열 관련 함수
print(len(d))
print(a.count('다'))
print(b.find('홍길동'))
print(b.index('홍길동'))

#문자열 삽입
print(','.join('가나다라'))

#공백 제거
#b= '       hello i\'m taehun      '
print(b.lstrip(),b.rstrip() + '!!')
print(b.strip())

#문자열 치환
print(b.replace('홍길동', '김길동'))

print(b.split()) #공백 , + - 기준으로 분리 가능