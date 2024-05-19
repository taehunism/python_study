# method 재정의
# 상속관계에서 부모 클래스의 메서드를 자식 클래스가 변경해서 정의하는 것
# 오버라이딩 하는 거임 
class Phone:
    def call(self):
        print("call")
    def receive(self):
        print("receive")
        
class SmartPhone(Phone):
    def call(self):
        print("video call")
        
sp = SmartPhone()
sp.call() #자식 클래스의 메서드
sp.receive() #부모 클래스의 메서드

p = Phone()
p.call()

#다형성(polymorphism)의 개념
#Poly - 다양한 morphism - 사상
class Animal:
    def sleep(self):
        print("sleep")

class Tiger(Animal):
    def sleep(self):
        print("tiger's sleep now")

class Rabbit(Animal):
    def sleep(self):
        print("rabbit's sleep now")
        
class Eagle(Animal):
    def sleep(self):
        print("eagle's sleep now")
        
animals = []
animals.append(Animal())
animals.append(Tiger())
animals.append(Rabbit())
animals.append(Eagle())

for ani in animals:
    ani.sleep()