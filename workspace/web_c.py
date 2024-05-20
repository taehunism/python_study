#웹 크롤링
#   웹 사이트를 정기적으로 접속하여 정보를 추출하는 기술
#웹 스크래핑
#   웹사이트에 있는 특정 정보를 추출하는 기술

#웹 크롤러 : 웹크롤링 기술로 만들어진 프로그램 -> 검색엔진: 네이버, 구글

#pip3 install requests


import requests

url = "https://n.news.naver.com/mnews/article/029/0002874422"
#서버에 접속안되면 headers 긁어와서 
#resp = requests.get(url, headers=headers); 로 실행
resp = requests.get(url);
print(resp) #출력값 200은 정상반응
print(resp.text) #페이지 소스보기의 내용