# Scope는 영역, 범위를 뜻함
# 변수를 사용할 수 있는 범위
# 전역, 지역으로 나뉨
# 전역 변수는 global
# 영역의 기준 -> 파일
# 어디서나 사용 가능

# 지역 변수는 local
# 함수 영역에 선언되어 함수 내에서만 사용 가능

x=10 # global

# def add(x): #local
#     x += 1
#     print(x)
#     return x
# x = add(10)
#
# print(x)

def add():
    global x # global x를 사용
    x+=1
add()
print(x)

# def outer(a,b):
#     def inner(c,d):
#         return c+d
#     return inner(a,b)

# r = outer(10,20)
# print(r)
#inner(10,20) # local function으로 사용 불가능

def outer(a,b):
    def inner(c,d):
        return c+d
    return inner

f=outer(10,20)
print(type(f))
r=f(10,20)
print(r)
#이름은 f지만 inner가 리턴되어 다른이름을 가진 함수가 됨

r = outer(10,20)(10,20)
# 첫째 괄호까지 함수의 리턴값 이후 뒤 매개변수는 리턴받은 함수의 매개변수


