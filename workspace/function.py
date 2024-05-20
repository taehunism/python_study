#함수
# y = f(x)
# 입력을 넣었을 때 출력을 뱉음. 시스템 비슷

# python 에서는 define -> def로 함수를 정의함
# 매개변수 생략 가능 그 후 콜론 -> def function():

# 함수를 실행 (call) -> function()

# def test():
#     print("hello")
#     print("i am taehun")
#
# test()
#
# print(type(test))

def gugu():
    for i in range(2,10):
        for j in range(1,10):
            print(f" {i} * {j} = {i*j}")

gugu()

#함수의 사용 목적은 무엇일까? -> 실행의 목적을 가짐 