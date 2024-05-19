#파일 입출력 개념
#input - 데이터 읽기
#output - 데이터 쓰기

#open()
#open(파일명, 모드, 인코딩)
#모드 r , w , a , b - 읽기, 쓰기, 추가, 바이너리 모드
#지정된 인코딩 값이 아닐 경우 파일이 깨짐

#파일 입출력 실습

# 쓰기
f = open('test.txt', 'w', encoding='utf-8') #가장 많이 사용하는 인코딩
# 기본값으로 사용하게되면 한글 사용 불가능
f.write("안녕하세요~\n")
f.close() # 꼭! close 해주어야함. 리소스 계속 할당됨

# 추가
f = open('test.txt', 'a', encoding='utf-8')
f.write('안녕하세요2')
f.close()

# 읽기
# f = open('test.txt', 'r', encoding='utf-8')
# txt = f.read()
# f.close()
# print(txt)
f = open('test.txt', 'r', encoding='utf-8')
while(True):
    txt = f.readline()
    print(txt) #end='' 로 하면 줄바꿈 안함 기본값 end='\n'
    if not txt: break
f.close()

# with를 쓰면 close를 안써줘도 됨. 가장 많이 쓰는 형태
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())