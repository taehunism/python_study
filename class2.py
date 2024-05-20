# #클래스 구성요소
# #클래스 변수
# #생성자
# #소멸자
# #메서드
# #전부 생략 가능
#
# class Member:
#     country = "대한민국"
#
#     def join(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print(self):
#         print(f"name : {self.name}")
#         print(f"age : {self.age}")
#
# print(Member.country)
#
# mem = Member()
# mem.join("홍길동", 30)
# mem.print()
#
# mem2 = Member()
# mem2.join("김길동",40)
# mem2.print()

class Member:
    country = "대한민국"

    def join(self, name, age):
        self.a = name
        self.b = age
    @classmethod
    def print(cls, a,b):
        print(f"name : {a}")
        print(f"age : {b}")

print(Member.country)
Member.print("홍길동", 30)
mem = Member()
mem.join("taehun",25)
print(mem.a)