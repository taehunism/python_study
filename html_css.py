# HTML : Hyper Text Markup Language
# 웹 페이지의 구조적 표현을 위해 사용하는 마크업 언어
# 텍스트, 이미지, 동영상 등 페이지 내에서 콘텐츠 작성 용도로 사용
# 태그로 이루어져 있음

#HTML 태그의 표현 형식
#<div id="title">안녕하세요</div>
#여는 태그<div>에 속성명(id)과 속성값("title")이 들어감 
#태그 내용 : 안녕하세요
#닫는 태그 </div>

#CSS : Cascading Style Sheets : 스타일 시트
#웹 페이지의 디자인적인 요소를 제어하는 기능
#색상, 크기, 위치 등 디자인적으로 꾸미는 용도로 사용
#내용은 HTML, 디자인은 CSS로 작성하게 됨

#크롤링 할 때 필요한 '선택자' 개념을 반드시 알아야 함
#속성을 선택하는 친구
#외워둬야하는 6가지 필수 선택자
#태그 선택자 ex) div
#아이디 선택자 ex) #title
#클래스 선택자 ex) .name
#속성 선택자 ex) div[class= 'abc']
#자식/ 자손 선택자 ex) 자식:div > a, 자손 : div a
#nth-child(n) (n번째 요소)

# #mArticle > div.head_view > h3

# mArticle id선택자
# > 는 자식 
# div 태그
# .rank_news 는 클래스
# ul 태그
# .list_news2 클래스
# 태그.선택자 > 태그 > 태그