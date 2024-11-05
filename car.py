class Car:
    def message(self) :
        print("I'm basic")
    
    def horn(self) :
        print("*beep beep*")
        
class FancyCar(Car) :
    def message(self):
        print("I'm fancy!")

c = FancyCar()
c.horn()