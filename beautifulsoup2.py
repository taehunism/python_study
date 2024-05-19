#request 모듈 연동 방법
#get() / post() 함수로 해당 url 데이터 저장
#저장한 문서 데이터를 통해 BeautifulSoup 객체 생성

import requests
from bs4 import BeautifulSoup
res = requests.get('https://v.daum.net/v/20240519140141781')
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.select_one('#mArticle > div.head_view > h3')
print(title.string)

res = requests.get('https://m.entertain.naver.com/ranking')
soup = BeautifulSoup(res.text, 'html.parser')

title = []
link = []

for text in soup.select('#ct > div > div.com_ranking.index > ul > li > a > div.tit_area > p'):
    title.append(text.string)
    link.append(text.attrs['class'])
    
print(len(title))

for i, _ in enumerate(title): # i 는 인덱스, _는 값인데 _를 썼다는건 안받겠다는거
    print(i, title[i], link[i])