#모듈이란?
#   변수, 함수, 클래스를 모아 놓은 파일

#모듈 사용방법
#   import 모듈명(파일명)
#   from 모듈명 import 함수명
#   from 모듈명 import 함수명1, 함수명2
#   from 모듈명 import *

#모듈 생성 및 학습
def plus(x,y):
    return x+y
def minus(x,y):
    return x-y

# 내가 여기서 이걸 실행하면 파일 이름 __name__ == __main__
# 다른 곳에서 불러오면 이름이 파일명 이름으로 나옴 module
if __name__ == "__main__":
    print(__name__)
    print('execute success')