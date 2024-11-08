class Car:
    # def message(self) :
    #     print("I'm basic")
    def __init__(self, s):
        self.sound = s
    
    def horn(self) :
        print(self.sound)
        
class FancyCar(Car) :
    # def message(self):
    #     print("I'm fancy!")
    def __init__(self, c):
        self.color = c
        
    def showColor(self):
        print(self.color)

c1 = Car("*beep beep*")
c = FancyCar("turquoise")
c1.horn()