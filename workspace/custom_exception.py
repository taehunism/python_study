# 사용자 정의 예외 처리
# 예외(Exception) 클래스를 상속 받음
# 강제로 예외를 발생시키는 방법
# raise 예외 클래스명

import builtins
#print(dir(builtins))
#dir() 함수는 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메서드를 가지고 있는지 알려줌

# raise ZeroDivisionError

class UserError(Exception):
    def __str__(self): #언더바 2개는 내부 로직
        return "로그인 에러"
    # pass

def login(id):
    if id=="admin":
        print("login")
    else :
        raise UserError

login("admin")

try:
    login("test")
except UserError as e:
    print(e)