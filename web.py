#정적/ 동적 페이지 추출 방법
#selenium 패키지를 이용한 동적 페이지 데이터 추출
import requests
from bs4 import BeautifulSoup

res = requests.get('https://n.news.naver.com/article/009/0005305281?cds=news_media_pc')
soup = BeautifulSoup(res.text, 'html.parser')

title = soup.select_one('#title_area > span')
print(title.string)


#현재 크롬 버전이 높아 크롬드라이버 사용이 어려워보임
# from selenium import webdriver
# driver = webdriver.Chrome('chromedriver')
# driver.get('https://n.news.naver.com/article/009/0005305281?cds=news_media_pc')
# soup = BeautifulSoup(driver.page_source, 'html.parser')
#comment = soup.select_one('선택자')
#print(comment.string)

#셀레니움 패키지를 이용해 동적 페이지 데이터를 추출 할 수 있음