#클래스 상품 설계도
#객체 제작된 상품
#객체 지향 프로그래밍에서 클래스와 객체에 대한 개념

class Car:
    def accell(self): #method를 정의하면 자동으로 self
        print("전진")
    def back(self):
        print("후진")

car1 = Car()
car2 = Car()

car1.accell()
car2.accell()

print(car1 == car2) #둘은 내용은 같지만 다른 객체
#실제 메로리에 저장된 주소가 다르기 때문
print(id(car1))
print(id(car2))

car1.color = "흰색"
car2.color = "검정"

print(car1.color)
print(car2.color)