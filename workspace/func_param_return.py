# 매개변수 - 파라미터
# 외부 데이터를 함수 내부로 전달해주기 위한 용도의 변수
# 함수 내부의 지역 변수(함수 내부에서만 사용가능)

# 리턴값
# 결과 값을 실행한 곳으로 돌려주는 역할
# 함수를 실행한 곳으로 돌아가는 역할(함수 중지)

def add(x,y):
    z = x+y
    return z

a=add(1,2)
print(a)

def div(x,y):
    return x/y
print(div(10,5))
print(div(y=5,x=10))

# *은 튜플형태로 전달하겠다는 의미
def test(*args):
    r = 0
    for v in args:
        r+=v
    return r
print(test(1,2,3,4,5))

# **은 딕셔너리 형태로 전달
def test2(**kwargs):
    #items라는 함수는 키와 벨류가 따로따로 리턴됨
    for key, value in kwargs.items():
        print(f"key : {key}, value : {value}")
test2(a=1)

def member(name, age=10, gender='여자'):
    print(f"이름은 {name}")
    print(f"나이는 {age}")
    print(f"성별은 {gender}")
member('홍길동', 30)


