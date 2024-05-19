# BeautifulSoup
# 파이썬으로 스크래핑을 할 수 있게 해주는 라이브러리
# HTML, XML에서 원하는 데이터를 추출
# 별도 설치 필요
#  python -m pip install --upgrade pip
#  pip install beautifulsoup4 

# from bs4 import BeautifulSoup
# bs = BeautifulSoup(문서객체, 'html.parser')

#데이터 추출 방법 5가지
#DOM 트리에서 계층적 구조로 추출
#find()
#find_all()
#select_one()
#select()

#html과 css 선택자를 활용해 실습

from bs4 import BeautifulSoup

#html 예시
html = """
<html>
<body>
    <h1>스크래핑</h1>
    <div>HTML정보 추출</div>
    <span>XML정보 추출</span>
</body>
</html>
"""
#html 파싱
soup = BeautifulSoup(html, 'html.parser')

#계층 구조로 추출
text1 = soup.html.body.h1
text2 = soup.html.body.div
text3 = soup.html.body.span

print(text1.string)
print(text2.string)
print(text3.string)

html = """
<html>
    <body>
        <h1 id='title'>스크래핑</h1>
        <div class='contents'>HTML정보 추출</div>
        <span>XML정보 추출</span>
    </body>
</html>
"""
soup = BeautifulSoup(html,'html.parser')

title = soup.find(id='title')
print(title.string)

contents = soup.find(class_='contents') # class는 예약어라 class_ 사용
print(contents.string)

#####
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('#title')
print(title.string)
contents = soup.select_one('.contents')
print(contents.string)

html = """
<html>
    <body>
        <a href='http://www.naver.com'>네이버</a>
        <a href='http://www.daum.net'>다음</a>
        <a href='http://www.google.com'>구글</a>
    </body>
</html>
"""
soup = BeautifulSoup(html,'html.parser')
datas = soup.select('a')
for v in datas:
    print(v.attrs['href'], v.string) #atrs = attributes(속성) ['href'] 주소 출력
    # v.string은 텍스트 출력