# class 생성자
# def __init__(self) 객체를 생성하는 역할, 자동으로 생성자 추가
# def __del__(self) 소멸자는 잘 안씀. 알아서 자동으로 해줌

class Car:
    #pass
    def __init__(self, name, color):
        print("init start")
        self.name = name
        self.color = color
    def __del__(self):
        del self.name
        del self.color
        print("del start")

car = Car("avante", 'black')
print(car.name)
print(car.color)