class Car:
    @staticmethod
    def start():
        print("Car Start..")

    @staticmethod
    def stop():
        print("Car Stop.")

#single inhritance
class Toyato_Car(Car):
    def __init__(self,brand):
        self.brand = brand

car1 = Toyato_Car("Supra")
car1.start()

#multi-level inheritance
class Fortuner(Toyato_Car):
    def __init__(self,type):
        self.type = type

car2 = Fortuner("SUV")
car2.start()



#multiple inheritance
class A:
    varA = "Welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

e1 = C()
print(e1.varC)
print(e1.varB)
print(e1.varA)