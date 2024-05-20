#콜백
#뒤(특정시점)에서 실행되는 함수
#함수도 자료형 중 하나이므로 매개변수로 전달 가능
#비동기적으로 다른 함수에게 호출되기 위해 함수로 전달

#람다
#단일문으로 표현되는 익명함수
#익명함수 : 이름이 없는 구현체만 존재하는 간단한 함수
#소스 상에서 한 번만 사용되는 기능이 필요할 때, 1회용으로 사용

#클로저
#독립적인 변수를 가지고 있는 함수
#내부 함수 개념을 이용하여 별도의 스코프 정의

#callback func
def calc(func, a,b):#func는 함수가 들어올 자리
    a += 10
    b += 20
    print(func(a,b)) #매개변수로 들어온 func를 실행

def plus(a,b):
    return a+b
def minus(a,b):
    return a-b

calc(plus,10,20)
calc(minus,50,10)

#lambda
#lambda 매개변수 : 리턴값
#일회용 실행
calc(lambda a,b : a+b, 10,20)
calc(lambda a,b : a-b, 50, 10)

def test():
    text=("안녕하세요")
    return lambda : text

#클로저(Closure)
#내부함수를 이용하여 지역 변수를 전역에서 사용
print(type(test()))
t = test()
print(t())

def test2(name):
    text = "안녕하세요 제 이름은 {}입니다.".format(name)
    return lambda : text

t1 = test2('홍길동')
t2 = test2('김길동')

print(t1())
print(t2())