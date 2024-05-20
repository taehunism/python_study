#객체지향 프로그램에서의 상속
#자식 클래스가 부모 클래스를 선택해서 물려 받음
#상속의 구조
#클래스1에 여러 객체가 있음
#클래스2에서는 클래스1의 객체가 다 필요하고, 추가적인 메소드가 필요
#이 때 클래스2는 클래스1의 객체를 상속받고, 추가적인 메소드를 구현하면 됨
class Phone:
    name = None
    company = None
    color = None

    def call(self):
        print("call")
    def receive(self):
        print("receive")
    def status(self):
        print(self.name)
        print(self.company)
        print(self.color)
class SmartPhone(Phone):
    def installApp(self):
        print("installing App")

sp = SmartPhone()
sp.name = "smartphone"
sp.company = "samsung"
sp.color = "black"
sp.call()
sp.receive()
sp.installApp()
sp.status()